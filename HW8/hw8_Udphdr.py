import socket
import struct
import binascii

class Udphdr:
    def __init__(self, src, dst, tot_len, check):
        self.src_port = src
        self.dst_port = dst
        self.tot_len = tot_len
        self.checksum = check


    def pack_Udphdr(self):
        packed = b''
        packed += struct.pack('!2H', self.src_port, self.dst_port)
        packed += struct.pack('!2H', self.tot_len, self.checksum)
        return packed


def unpack_Udphdr(buffer):
    unpacked = struct.unpack('!4H', buffer[:8])
    return unpacked
    
def getSrcPort(unpacked_udpheader):
    return unpacked_udpheader[0]

def getDstPort(unpacked_udpheader):
    return unpacked_udpheader[1]

def getLength(unpacked_udpheader):
    return unpacked_udpheader[2]

def getChecksum(unpacked_udpheader):
    return unpacked_udpheader[3]


udp = Udphdr(5555, 80, 1000, 0xFFFF)
packed_Udphdr = udp.pack_Udphdr()

unpacked_udphdr = unpack_Udphdr(packed_Udphdr)

print(binascii.b2a_hex(packed_Udphdr))
print(unpacked_udphdr)
print('Source Port:{} Destination Port:{} Length:{} Checksum:{}'.format(getSrcPort(unpacked_udphdr), getDstPort(unpacked_udphdr), getLength(unpacked_udphdr), getChecksum(unpacked_udphdr)))
