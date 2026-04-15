import socket
def scan_port(ip, port):
    try:
        sock = socket.socket()
        sock.settimeout(1)
        sock.connect((ip, port))
        print(f"[+] Port {port} is OPEN")
        sock.close()
    except:
        pass
    
target_ip = input("Enter the IP address: ")
for port in range(1, 1025):
    scan_port(target_ip, port)