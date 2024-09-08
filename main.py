import pyfiglet
import sys
import socket
from datetime import datetime
import threading
from queue import Queue

# ASCII Banner
ascii_banner = pyfiglet.figlet_format(" AASHWAY PORT SCANNER")
print(ascii_banner)

# Defining a target
if len(sys.argv) == 2:
    # Translate hostname to IPv4
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid amount of arguments. Usage: python script.py <target>")
    sys.exit()

# Add Banner
print("-" * 50)
print("Scanning Target: " + target)
print("Scanning started at: " + str(datetime.now()))
print("-" * 50)

# Dictionary of common ports and their corresponding protocols
port_protocols = {
    20: 'FTP (Data)',
    21: 'FTP (Control)',
    22: 'SSH',
    23: 'Telnet',
    25: 'SMTP',
    53: 'DNS',
    67: 'DHCP (Server)',
    68: 'DHCP (Client)',
    69: 'TFTP',
    80: 'HTTP',
    110: 'POP3',
    119: 'NNTP',
    123: 'NTP',
    135: 'Microsoft RPC',
    137: 'NetBIOS Name Service',
    138: 'NetBIOS Datagram Service',
    139: 'NetBIOS Session Service',
    143: 'IMAP',
    161: 'SNMP',
    194: 'IRC',
    443: 'HTTPS',
    445: 'Microsoft DS (Active Directory/SMB)',
    465: 'SMTPS',
    514: 'Syslog',
    515: 'LPD (Printer)',
    587: 'SMTP (Submission)',
    993: 'IMAPS',
    995: 'POP3S',
    1080: 'SOCKS Proxy',
    1433: 'Microsoft SQL Server',
    1434: 'Microsoft SQL Monitor',
    1521: 'Oracle DB',
    1701: 'L2TP',
    1723: 'PPTP',
    1812: 'RADIUS (Authentication)',
    1813: 'RADIUS (Accounting)',
    2049: 'NFS',
    2082: 'cPanel',
    2083: 'cPanel (Secure)',
    2086: 'WHM',
    2087: 'WHM (Secure)',
    3306: 'MySQL',
    3389: 'RDP (Remote Desktop)',
    5432: 'PostgreSQL',
    5500: 'VNC Remote Desktop',
    5631: 'PCAnywhere',
    5900: 'VNC',
    6000: 'X11',
    8080: 'HTTP Proxy',
    8443: 'HTTPS (Alternate)',
    8888: 'HTTP (Alternate)',
    9100: 'JetDirect (Printer)',
    10000: 'Webmin',
    # You can continue adding more ports and protocols as needed
}

# Function to scan a single port
def scan_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            protocol = port_protocols.get(port, 'Unknown Protocol')
            print(f"Port {port} is open ({protocol})")
        s.close()
    except KeyboardInterrupt:
        print("\n Exiting Program !!!!")
        sys.exit()
    except socket.gaierror:
        print("\n Hostname could not be resolved !!!!")
        sys.exit()
    except socket.error:
        print("\n Server not responding !!!!")
        sys.exit()

# Threading function to speed up the scanning
def threader():
    while True:
        port = q.get()
        scan_port(port)
        q.task_done()

# Create a queue and launch thread workers
q = Queue()

# Number of threads (tune this number based on your system)
num_threads = 100

# Creating threads
for x in range(num_threads):
    t = threading.Thread(target=threader)
    t.daemon = True  # Daemon threads exit when the main program exits
    t.start()

# Assign tasks to the queue
for port in range(1, 65535):  # Scan all ports from 1 to 65535
    q.put(port)

# Wait until all tasks are completed
q.join()

# Print completion message
print("-" * 50)
print(f"Scanning finished at: {str(datetime.now())}")
print("Scan complete. All ports have been scanned.")
print("-" * 50)
