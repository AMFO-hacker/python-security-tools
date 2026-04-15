import ftplib
import socket

def anonLogin(hostname):
    try:
        ftp = ftplib.FTP(hostname, timeout=5)
        response = ftp.login('anonymous', '')
        
        if "230" in response:
            print(f"[+] {hostname} - Anonymous Login Allowed")
            ftp.quit()
            return True
        else:
            print(f"[-] {hostname} - Login Denied")
            ftp.quit()
            return False

    except ftplib.error_perm:
        print(f"[-] {hostname} - Permission Denied (530)")
        return False

    except socket.timeout:
        print(f"[!] {hostname} - Connection Timed Out")
        return False

    except ConnectionRefusedError:
        print(f"[!] {hostname} - Port 21 Closed")
        return False

    except Exception as e:
        print(f"[!] {hostname} - Error: {e}")
        return False


if __name__ == "__main__":
    target = input("Enter target IP: ")
    anonLogin(target)