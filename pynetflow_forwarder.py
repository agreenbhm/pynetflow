import socket
import pynetflow
import struct
import pickle
import netaddr

class NetflowForwarder:

    def __init__(self, localip="", localport=1514, graphiteip="127.0.0.1", graphiteport=2004, networks=[], verbose=False, noGraphite=False):

        self.localip = localip
        self.localport = localport
        self.graphiteip = graphiteip
        self.graphiteport = graphiteport
        self.networks = networks
        self.numnets = 0
        self.verbose = verbose
        self.noGraphite = noGraphite

    def run(self):

        try:
            self.server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.server.bind(("", self.localport))
        except Exception as e:
            print "Error opening receiver socket: " + e.message
            exit(1)

        if not self.noGraphite:
            try:
                self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.client.connect((self.graphiteip, self.graphiteport))
            except Exception as e:
                print "Error connecting to Graphite socket: " + e.message
                exit(1)

        print "Listening on %s:%s" % ("0.0.0.0" if self.localip == "" else self.localip, self.localport)

        netobjs = []
        for net in self.networks:
            netobjs.append(netaddr.IPNetwork(net))
        self.numnets = len(netobjs)

        while 1:
            try:
                data, addr = self.server.recvfrom(65536)
                nf = pynetflow.Netflow(addr[0], data)
                if not self.noGraphite:
                    nf.header['sensor'] = nf.header['sensor'].replace(".", "_")
                    inpath = "network.bandwidth.probes.%s.%s.%s.ingress"
                    outpath = "network.bandwidth.probes.%s.%s.%s.egress"
                    pduList = []
                    if self.verbose:
                        print "\nHeader: " + str(nf.header) + "\n"
                    for pdu in nf.data:
                        if self.numnets > 0:
                            for net in netobjs:
                                if netaddr.IPNetwork(pdu['src_addr']).value >= net.first or netaddr.IPNetwork(pdu['src_addr']).value <= net.last:
                                    pduList.append((inpath % (nf.header['sensor'], "subnets", str(net.network).replace(".", "_")), (nf.header['unix_secs'], int(pdu['dOctets']))))
                                if netaddr.IPNetwork(pdu['dst_addr']).value >= net.first or netaddr.IPNetwork(pdu['dst_addr']).value <= net.last:
                                    pduList.append((outpath % (nf.header['sensor'], "subnets", str(net.network).replace(".", "_")), (nf.header['unix_secs'], int(pdu['dOctets']))))
                        else:
                            pduList.append((inpath % (nf.header['sensor'], "interfaces", pdu['input']), (nf.header['unix_secs'], int(pdu['dOctets']))))
                            pduList.append((outpath % (nf.header['sensor'], "interfaces", pdu['output']), (nf.header['unix_secs'], int(pdu['dOctets']))))

                        if self.verbose:
                            print "Data: " + str(pdu) + "\n"

                    if self.verbose:
                        print "======================"

                    payload = pickle.dumps(pduList, protocol=2)
                    header = struct.pack("!L", len(payload))
                    message = header + payload
                    self.client.send(message)

                else:
                    print "\nHeader: " + str(nf.header) + "\n"
                    for pdu in nf.data:
                        print "Data: " + str(pdu) + "\n"
                    print "======================"

            except Exception as e:
                print "Error sending data: " + e.message