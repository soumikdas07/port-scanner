# 🔍 Python Port Scanner

A fast, multithreaded port scanner built with Python. This tool scans the first 1024 ports of any target IP address or domain name to identify open ports.

---

## ⚙️ Features

- Scans ports from 1 to 1024
- Multithreaded scanning using `concurrent.futures`
- Lightweight — uses only Python standard libraries
- Clean and minimal CLI interface

---

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/soumikdas07/port-scanner.git
cd port-scanner
```

### 2. Run the Script

```bash
python scanner.py
```

### 3. Sample Output

```bash
Enter target IP or domain: scanme.nmap.org
Scanning scanme.nmap.org for open ports (1-1024)...
[+] Port 80 is open
[+] Port 22 is open
```

## ⚙️ How It Works

```bash
- The script uses Python's `socket` module to try connecting to ports 1–1024.
- It uses `concurrent.futures.ThreadPoolExecutor` to scan ports in parallel.
- If a port responds (connection successful), it's reported as open.
```
