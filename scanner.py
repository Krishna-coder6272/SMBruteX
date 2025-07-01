# === modules/scanner.py ===
import socket

def port_open(ip, port=445):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(2)
        return s.connect_ex((ip, port)) == 0

def detect_os_smb(ip):
    return ("Windows", "SMBv2")  # Placeholder for real fingerprinting
