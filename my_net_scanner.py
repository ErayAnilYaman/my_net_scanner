import scapy.all as scapy
import optparse
#1) CREATING ARP REQUEST
#2) BROADCAST
#3) RESPONSE
def get_user_input():
    parse_object = optparse.OptionParser();
    parse_object.add_option("-i","--ip_address",dest="ip_address",help="Enter ip address");
    (user_input,args) = parse_object.parse_args()
    if not user_input.ip_address:
        print("Enter true ip address");
    return user_input;

def scan_my_network(user_input):
    arp_request_packet = scapy.ARP(pdst=user_input.ip_address)
    # scapy.ls(scapy.ARP())
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    # scapy.ls(scapy.Ether())

    combined_packet = broadcast_packet / arp_request_packet;
    # bu iki paketi birbirne baglamya yardim eder.
    (answered_list,unanswered_list) = scapy.srp(combined_packet,timeout=1)
    answered_list.summary()



scan_my_network(get_user_input())


