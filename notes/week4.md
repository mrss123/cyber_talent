## NMAP

# whatis NMAP?
- open source and free network mapper 
- used for network discovery and sec auditing 
- it uses raw IP packets to determine what hosts are available on the network 
- consists 
	- GUI `zenmap`
	- `ncat` flezible data transfer and debugging tool 
	- `ndiff` to compare scan results 
	- `nping ` packet generation and response tool
# used_for 
- network exploration 
	- port scanning 
	- OS fingerprinting 
	- service detection 
	- security auditing and pentesting 
	- network managment 
	- scriptable interaction  (written with lua)
# interaction
  - layer 4 (transport layer)
		- TCP (SYN)
		- SCTp
		- UDP (ICMP)
		- SYN scan -sS
		- versions -sV
	- layer 3 (network layer)
		- for host discovery 
		- ICMP 
		- traceroute 
	- layer 2 (datalink)
		- if in the same network 
		- to find MAC 
# TCP
 -using SYN to see if OPEN or RST CLOSED 
	- stealth scan `-sS` 
	- `sT` for all users
# UDP 
- ICMP errors 
	- `-sU` 
	- if error recived it is closed  ICMP unreachable if not it is open and filtered 
	- very slow 
# OS_DETCTION 
 - it tries to identify what OS is running using what version 
	- and helps to minimize effort and have more specific target 
# NSE 
- allows user to write and share LUA based scripts
	- for advanced network discovery 
		- vuln
		- backdoor detection 
		- elite version detection 
		- `--script` `brute , vuln , default , safe , intrusive , dicovery `
# conmmon_flags 
 - `sS` stealth
	- `sV` version 
	- `O` os 
	- `p-` all ports 
	- `Pn` skip host discovery 
	- `A` aggressive scan 
	- `T4` fast timing 
	- `o` output file 
	- `oA` out file in normal , xml and grepable format 
	- `oG` grepable output 
	- `oX` send only xml files 
	- SMAP Passive recon 
# difference
   - `sS` stealth scan : only checks if it is up no handshake  (IDS) , fast and efficient 
	  - `sT` connect scan : complete 3 way handshake , very noisy , easy to be detected , no root usage , to see hosts that complete handshakes
# filtered 
  - can't detect what is because of  a fire wall 
	- if UDP means open
	- droped packet
# firewall
  - packet fragmentation `f, --mtu`
		- to easily pass traffic 
	- source port manipulation 
		-  admins often make network to trust if it is coming from specific ports
	- decoy scanning 
		- obsecure the attackerrs IP by making it like it is coming from multiple IP addresses
		- and the target won't be able to see which is responsible for the scan
		- `-D , decoy1, decoy2, decoy3 , decoy4`
	- TCP ACK scan
		- make it like it is already from esablished connection 
	- MAC spoofing 
# xmas
  - `sX
	- sends a malformed packets 
	- if open it don't respond if close snt RST error 
	- ineffective for modern networks 
