# In-This-Subnet
Python program to determine if a given IPv4 address is in a given subnet.
The IP address is passed as a string representation of a 32-bit unsigned int and the subnet is passed as a string representation of a CIDR subnet (e.g., "98.210.237.192/26"). The program outputs True if the IPv4 address is in the subnet, and False otherwise. 
The program is built on Python 2.7. It accepts 3 parameters :
1. the ip address in 32 bit unsigned int
2. the cidr  range
3. optional parameter for filename that stores ipaddress ( in 32 bit unsigned) and cidr range. If this parameter is provided, then the output is generated in output.txt file that is located at the same level in the code repo.

--This repo contains--
  1. socketprogram.py
  2. ip_subnet.txt
  3. output.txt 
  
-- How to run the program--

python socketprogram.py ip_address cidr_range filename(optional param)

-- Examples --
1. The execution returns True if ip address is found in the cidr provided
               python socketprogram.py 0x62D2EDC2 "98.210.237.192/26"
               Output: True
2. The  execution returns False if ip address is not found in the cidr provided
              python socketprogram.py 0x62DCEDC9 "98.210.237.192/26"
              Output: False
3. The  execution returns True/False depending on if the ip address is present in cidr. In addition since we have passed the optional parameter for filename (ip_subnet.txt), it will also output the result in output.txt file located in same level of the code repo
              python socketprogram.py 0x62D2EDC2 "98.210.237.192/26" ip_subnet.txt
              Output: True
              ip_subnet.txt
The output is available in output.txt located inside the code repo

Contents of the ip_subnet.txt file
0x62D2EDC0 98.210.237.192/26
0x62D2EDC2 98.210.237.192/26
0x62D2EDC3 98.210.237.192/26
0x62DCEDC9 98.210.237.192/26

Contents of the output.txt file
ip address: 0x62D2EDC0 present in cidr range: 98.210.237.192/26
 is: True
ip address: 0x62D2EDC2 present in cidr range: 98.210.237.192/26
 is: True
ip address: 0x62D2EDC3 present in cidr range: 98.210.237.192/26
 is: True
ip address: 0x62DCEDC9 present in cidr range: 98.210.237.192/26 is: False
