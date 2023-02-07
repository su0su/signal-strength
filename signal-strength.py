from scapy.all import *

class beacon:
    def __init__(self, interface, mac):
        self.interface= interface
        self.mac = mac
        self.rssi = None

def packet_handler(pkt):
    if pkt.haslayer(Dot11) and pkt.type==0 and pkt.subtype==8:
            if pkt.haslayer(Dot11Beacon) or pkt.haslayer(Dot11ProbeResp):
                if pkt.addr2 == b.mac.lower() :              
                    try : 
                        radiotap = pkt.getlayer(RadioTap)
                        b.rssi = radiotap.dBm_AntSignal
                    except:
                        b.rssi=-1000    
                    print ("signal-strength={}".format(b.rssi))
                
if __name__ == "__main__":
    inf=interface=sys.argv[1]
    m=sys.argv[2]
    b=beacon(inf, m)
    sniff(iface=b.interface, prn=packet_handler)
    