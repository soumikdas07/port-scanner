import socket
import concurrent.futures

def scan_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            result = s.connect_ex((ip, port))
            if result == 0:
                print(f"[+] Port {port} is open")
    except Exception as e:
        print(f"[-] Error scanning port {port}: {e}")

def run_scanner():
    target = input("Enter target IP or domain: ").strip()
    print(f"Scanning {target} for open ports (1-1024)...")

    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        for port in range(1, 1025):
            executor.submit(scan_port, target, port)

if __name__ == "__main__":
    run_scanner()
