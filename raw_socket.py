from scapy.all import sniff, IP 
 
def packet_callback(pkt): 
    if IP in pkt: 
        proto = pkt[IP].proto 
        if proto == 1: name = "ICMP" 
        elif proto == 6: name = "TCP" 
        elif proto == 17: name = "UDP" 
        else: name = "Unknown" 
 
        print(f"Protocol: {name}") 
        print(f"Source IP: {pkt[IP].src}") 
        print(f"Destination IP: {pkt[IP].dst}") 
        print("-" * 40) 
 
sniff(iface="Wi-Fi", prn=packet_callback, filter="ip", store=0)