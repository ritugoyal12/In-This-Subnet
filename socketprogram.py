import sys
import socket,struct
from socket import error as socket_error

def addressInNetwork(ip,net):
    "Is an address in a network"
    try:
        ipaddr = struct.unpack('>L',socket.inet_aton(ip))[0]
        netaddr,bits = net.split('/')
        netmask = struct.unpack('>L',socket.inet_aton(netaddr))[0]
        ipaddr_masked = ipaddr & (4294967295<<(32-int(bits)))   # Logical AND of IP address and mask will equal the network address if it matches
        if netmask == netmask & (4294967295<<(32-int(bits))):   # Validate network address is valid for mask
                return ipaddr_masked == netmask
        else:
                print "***WARNING*** Network",netaddr,"not valid with mask /"+bits
                return ipaddr_masked == netmask
    except socket_error as serr:
        return serr

# samples below for testing
#ip_address="0x62DCEDD7"
#ip_address="0x62D2EDD7"
#cidr_range="98.210.237.192/26"
#cidr_range="172.210.237.192/26"

def process_filename(filename):
    file = open(filename, "r")
    file_output = open("output.txt", "w+")

    for line in file:
        #print(line)

        network_details=line.split(" ")
        ip_address=network_details[0]
        #print('ip_address is'+ip_address)
        cidr=network_details[1]
        #print('cidr is' + cidr)
        results=addressInNetwork(str(ip_address),str(cidr))
        #print(results)
        #file_output.write("rohan"+"\n")
        #file_output.write("ip address: "+ip_address+" present in cidr range: "+cidr+" is: "+results+"\n")
        file_output.write("ip address: "+ip_address+" present in cidr range: "+str(cidr)+" is: "+str(results)+"\n")
    #file_output.close()
    print('the output is available in output.txt located inside the code repo')
    file.close()




def main(args,**kwargs):
    #ip_address = input("Please input the ip address as 32-bit unsigned int: ") # in case we need explicit input
    #cidr_range=input("Please input the cidr range: ")  # in case we need explicit input
    ip_address=args[1]
    cidr_range=args[2]

    results=addressInNetwork(str(ip_address),str(cidr_range))
    print(results) #outputs true or false
    try:
        if args[3] is not None:
            filename=str(args[3])
            print(filename)
            process_filename(filename)

    except:
        filename=""

if __name__ == '__main__':
    main(sys.argv)