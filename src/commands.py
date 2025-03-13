import socket
import subprocess

def whois_lookup(domain):
    """Perform WHOIS lookup."""
    try:
        result = subprocess.run(["whois", domain], capture_output=True, text=True)
        return result.stdout.strip() if result.stdout else "No WHOIS information found."
    except Exception as e:
        return f"Error: {e}"

def nslookup(domain):
    """Perform NS lookup."""
    try:
        result = subprocess.run(["nslookup", domain], capture_output=True, text=True)
        return result.stdout.strip() if result.stdout else "No NSLOOKUP information found."
    except Exception as e:
        return f"Error: {e}"

def port_scan(target, ports=[21, 22, 25, 53, 80, 443, 3306, 8080]):
    """Scan specified ports on a target."""
    open_ports = []
    try:
        for port in ports:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(1)
                if sock.connect_ex((target, port)) == 0:
                    open_ports.append(port)
        return f"Open ports on {target}: {open_ports}" if open_ports else "No open ports found."
    except Exception as e:
        return f"Error scanning ports: {e}"

def ping_sweep(network):
    """Ping sweep a subnet (e.g., 192.168.1)."""
    live_hosts = []
    try:
        for i in range(1, 255):
            ip = f"{network}.{i}"
            result = subprocess.run(["ping", "-c", "1", ip], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            if result.returncode == 0:
                live_hosts.append(ip)
        return f"Live hosts: {live_hosts}" if live_hosts else "No live hosts found."
    except Exception as e:
        return f"Error during ping sweep: {e}"

def banner_grab(target, port):
    """Grab the service banner of an open port."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(2)
            sock.connect((target, port))
            sock.send(b"HEAD / HTTP/1.1\r\nHost: target\r\n\r\n")
            banner = sock.recv(1024).decode().strip()
        return f"Banner from {target}:{port} -> {banner}"
    except Exception:
        return f"Could not grab banner for {target}:{port}."
