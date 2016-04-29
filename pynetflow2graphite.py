import argparse
from pynetflow_forwarder import NetflowForwarder

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Netflow to Graphite forwarder")
    parser.add_argument("--interface", "-i",  nargs='?', help="Local listening interface IP, default=0.0.0.0", default="0.0.0.0")
    parser.add_argument("--localport", "-p",  nargs='?', help="Local listening port, default=1514", default=1514)
    parser.add_argument("--graphiteip", "-g",  nargs='?', help="Graphite server IP, default=127.0.0.1", default="127.0.0.1")
    parser.add_argument("--graphiteport", "-f", nargs='?', help="Graphite server port, default=2004", default=2004)
    parser.add_argument("--subnets", "-s", nargs='*', help="Subnets to monitor, formatted as: 192.168.0.0/24", default="")
    parser.add_argument("--verbose", "-v", help="Print NetFlow PDUs to console", action="store_true")
    parser.add_argument("--nographite", "-n", help="Don't forward to Graphite (print to console)", action="store_true")
    args = parser.parse_args()

    nfForwarder = NetflowForwarder(args.interface, args.localport, args.graphiteip, args.graphiteport, args.subnets, args.verbose, args.nographite)
    nfForwarder.run()


