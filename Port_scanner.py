import socket
import termcolor

def scan(target,ports):
    print('\n'+'Starting Scan For '+str(target))
    for port in range(1,ports):
        scan_port(target,port)

def scan_port(ipaddress,port):
    try:
        sock=socket.socket()
        sock.connect((ipaddress,port))
        print("[+] Port Opeened "+str(port))
        sock.close()
    except:
        pass
        #print("[-] Port Closed "+str(port))

targets=input("[*] Enter Target To Scan(split by [,]): ")
ports=int(input("[*] Enter How Many Ports You Want To Scan: "))

if ',' in targets:
    print("[*] Scanning Multiple Targets")
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(' '),ports)
else:
    scan(targets,ports)
