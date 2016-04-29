class Netflow:

    def __init__(self, sensor, raw):

        self.rawdata = raw.encode('hex')
        self.sensor = sensor
        self.header = {}
        self.data = {}
        try:
            self.header = {
                'sensor': self.sensor,
                'version': int("0x" + self.rawdata[0:4], 0),
                'count': int("0x" + self.rawdata[4:8], 0),
                'sys_uptime': int("0x" + self.rawdata[8:16], 0),
                'unix_secs': int("0x" + self.rawdata[16:24], 0),
                'unix_nsecs': int("0x" + self.rawdata[24:32], 0),
                'flow_sequence': int("0x" + self.rawdata[32:40], 0),
                'engine_type': int("0x" + self.rawdata[40:42], 0),
                'engine_id': int("0x" + self.rawdata[42:44], 0),
                'sampling_interval': int("0x" + self.rawdata[44:48], 0)
            }

            try:
                tmpdata = self.rawdata[48:]
                dataList = []
                for i in xrange(0, self.header['count']):
                    dataList.append(tmpdata[i * 96:(i * 96) + 96])

                self.data = []
                for i in dataList:
                    dataDict = {
                        'src_addr': str(int("0x" + i[:2], 0)) + '.' + str(int("0x" + i[2:4], 0)) + '.' +
                                    str(int("0x" + i[4:6], 0)) + '.' + str(int("0x" + i[6:8], 0)),

                        'dst_addr': str(int("0x" + i[8:10], 0)) + '.' + str(int("0x" + i[10:12], 0)) + '.' +
                                    str(int("0x" + i[12:14], 0)) + '.' + str(int("0x" + i[14:16], 0)),

                        'next_hop': str(int("0x" + i[16:18], 0)) + '.' + str(int("0x" + i[18:20], 0)) + '.' +
                                    str(int("0x" + i[20:22], 0)) + '.' + str(int("0x" + i[22:24], 0)),

                        'input': str(int("0x" + i[24:28], 0)),

                        'output': str(int("0x" + i[28:32], 0)),

                        'dPkits': str(int("0x" + i[32:40], 0)),

                        'dOctets': str(int("0x" + i[40:48], 0)),

                        'first': str(int("0x" + i[48:56], 0)),

                        'last': str(int("0x" + i[56:64], 0)),

                        'tcp_flags': str(int("0x" + i[74:76], 0)),

                        'prot': str(int("0x" + i[76:78], 0)),

                        'tos': str(int("0x" + i[78:80], 0)),

                        'src_as': str(int("0x" + i[80:84], 0)),

                        'dst_as': str(int("0x" + i[84:88], 0)),

                        'src_mask': str(int("0x" + i[88:90], 0)),

                        'dst_mask': str(int("0x" + i[90:92], 0)),

                    }

                    self.data.append(dataDict)

            except Exception as e:
                print "Error parsing data: " + e.message
                pass

        except Exception as e:
            print "Error parsing header: " + e.message
            pass