import ipinfo
import threading
import socket
 
def scan_port (target ,port , open_port):
    try :
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1.5)
        result = sock.connect_ex((target, port))
        sock.close()
        if result == 0:
            open_port.append(port)
            print(f"^-^ port {port} is open")
    except:
        pass
def get_dns_name (ip):
    try:
        hostname, _, _ = socket.gethostbyaddr(ip)
        return hostname
    except socket.herror:
        return "no name found"
def getip (hostname):
    try:
        ip = socket.gethostbyname(hostname)
        return ip
    except socket.gaierror:
        return None
def port_scanner(target, start_port=1, end_port=2000):   
    print(f"\nStarting port scan on {target} ...")         
    open_ports = []                                      
    threads = []                                         
    
    for port in range(start_port, end_port + 1):         
        t = threading.Thread(target=scan_port, args=(target, port, open_ports))  
        threads.append(t)                                
        t.start()                                        
        if len(threads) >= 200:                          
            for t in threads:                            
                t.join()
            threads = []                                 
    for thread in threads:
        thread.join()                                    
    print(f"\nScan finished. Open ports: {sorted(open_ports)}")
print ("-"*50)
print ("choose")
print ("1. IP Address")
print ("2. WEB name")
print ("-"*50)
choice = int (input ("enter here: "))

access_token = '098c0bb5969c4f' 
handler = ipinfo.getHandler(access_token)
handler._request_timeout =10
try: 
    if choice not in (1,2):
        print ("please enter 1 or 2")
except ValueError:
    print ("enter a number only")


if choice == 1:
    print ("-"*50)
    print ("choose")
    print ("1. location of the ip addres")
    print ("2. Nmap port scan ")
    print ("-"*50)
    choice2= int (input("enter here: "))
    enterIP = input ("enter IP address separeated by commas : ")
    ip_list = [ip.strip() for ip in enterIP.split(',')]
    
    details = handler.getDetails(enterIP)
    details = handler.getDetails('8.8.8.8')
    try: 
        if choice not in (1,2):
            print ("please enter 1 or 2")
    except ValueError:
        print ("enter a number only")
    if choice2 == 1:
        for ip in ip_list :
            print (f"processing IP: {ip}")
            try:    
                details = handler.getDetails(ip)
                print ('-'*50)
                print (f"IP : {ip} resolves {get_dns_name(ip)}")
                print (f"ISP: {getattr(details, 'org' , 'N/A')}")
                print (f"city: {details.city}")
                print (f"region: {details.region}")
                print (f"country {details.country_name}")
                print (f"location: {details.loc}")
                print ('-'*50)
            except Exception as e:
                print( f" error fetching data for {ip}: {e}")
    if choice2 == 2:
        for ip in ip_list:
            try:
                port_scanner(ip, 1,1024)
            except Exception as e:
                print (f"error fetching data for {ip} : {e}")
if choice == 2:
    print ("-"*50)
    web_name = input ("enter a website name: ").strip()
    target_ip = getip(web_name)
    if target_ip:
        print (f"{web_name} got resolved: {target_ip}")
    else:
        print("could not resolve the web name")
    print ("-"*50)
    print ("1. scan resolved ip addres location")
    print ("2. scan ip port")
    choice2= int (input("enter here: "))
    ip_list = [ip.strip() for ip in target_ip.split(',')]
    
    details = handler.getDetails(target_ip)
    details = handler.getDetails('8.8.8.8')
    try: 
        if choice not in (1,2):
            print ("please enter 1 or 2")
    except ValueError:
        print ("enter a number only")
    if choice2 == 1:
        for ip in ip_list :
            print (f"processing IP: {ip}")
            try:    
                details = handler.getDetails(ip)
                print ('-'*50)
                print (f"IP : {ip} resolves {get_dns_name(ip)}")
                print (f"ISP: {getattr(details, 'org' , 'N/A')}")
                print (f"city: {details.city}")
                print (f"region: {details.region}")
                print (f"country {details.country_name}")
                print (f"location: {details.loc}")
                print ('-'*50)
            except Exception as e:
                print( f" error fetching data for {ip}: {e}")
    if choice2 == 2:
        for ip in ip_list:
            try:
                port_scanner(ip, 1,1024)
            except Exception as e:
                print (f"error fetching data for {ip} : {e}")
        
    
