import subprocess
import optparse
import re

def print_banner():
    banner = """
    ██████╗ ██╗      █████╗  ██████╗██╗  ██╗██╗    ██╗███████╗████████╗
    ██╔══██╗██║     ██╔══██╗██╔════╝██║ ██╔╝██║    ██║██╔════╝╚══██╔══╝
    ██████╔╝██║     ███████║██║     █████╔╝ ██║ █╗ ██║███████╗   ██║   
    ██╔═══╝ ██║     ██╔══██║██║     ██╔═██╗ ██║███╗██║╚════██║   ██║   
    ██║     ███████╗██║  ██║╚██████╗██║  ██╗╚███╔███╔╝███████║   ██║   
    ╚═╝     ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ ╚══╝╚══╝ ╚══════╝   ╚═╝   
                       BlackHatWZ13 -  MacAddress_Changer                       
    """
    print(banner)
print_banner()

def get_argument():
    parser = optparse.OptionParser()
    parser.add_option("-i", dest="net_interface", help="This place is for network interface")
    parser.add_option("-m", dest="mac_address", help="This place is for a new mac address")
    options, arguments = parser.parse_args()   #عشان استقبل القيم بتاعتهم

    if not options.net_interface:
        parser.error("Please put your interface card please type -h for help")

    if not options.mac_address:
        parser.error("Please put a new mac address please type -h for help")

    return options


def mac_changer(net_interface, mac_address):
    subprocess.call("ifconfig "+net_interface+" down", shell=True)
    subprocess.call("ifconfig "+net_interface+" hw ether "+mac_address+" ", shell=True)
    subprocess.call("ifconfig "+net_interface+" up", shell=True)

options = get_argument()
mac_changer(options.net_interface, options.mac_address)

print("\n[+] Change MAC Address for "+options.net_interface+" to " +options.mac_address+"\n")


subprocess.call("ifconfig ", shell=True)
