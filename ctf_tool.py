#!/usr/bin/env python3
# ctf_tool.py
#
# CTF Multitool - helper script for TryHackMe/CTF labs
# Javid üçün hazırlanıb :)

import argparse
import subprocess
import socket
import hashlib
import base64
import os

# ===============================
# 1. Recon / Scanner
# ===============================
def port_scan(host, ports):
    print(f"[+] Scanning {host} on ports {ports}")
    start, end = map(int, ports.split("-"))
    for port in range(start, end+1):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            res = s.connect_ex((host, port))
            if res == 0:
                print(f"[OPEN] {port}")
            s.close()
        except:
            pass

def nmap_scan(target):
    print(f"[+] Running Nmap scan on {target}")
    subprocess.run(["nmap", "-sC", "-sV", "-oN", "nmap_scan.txt", target])

# ===============================
# 2. Hash Tools
# ===============================
def hash_generate(text, htype):
    if htype == "md5":
        return hashlib.md5(text.encode()).hexdigest()
    elif htype == "sha1":
        return hashlib.sha1(text.encode()).hexdigest()
    elif htype == "sha256":
        return hashlib.sha256(text.encode()).hexdigest()

def hash_crack(target_hash, htype, wordlist):
    print(f"[+] Cracking {htype} hash {target_hash}")
    with open(wordlist, "r", encoding="utf-8", errors="ignore") as f:
        for word in f:
            word = word.strip()
            candidate = hash_generate(word, htype)
            if candidate == target_hash:
                print(f"[+] Found password: {word}")
                return
    print("[-] Not found in wordlist")

# ===============================
# 3. Encoding / Decoding
# ===============================
def encode_b64(text):
    return base64.b64encode(text.encode()).decode()

def decode_b64(text):
    return base64.b64decode(text).decode()

# ===============================
# 4. External Tools Wrappers
# ===============================
def gobuster_dir(url, wordlist):
    print(f"[+] Running Gobuster on {url}")
    subprocess.run(["gobuster", "dir", "-u", url, "-w", wordlist])

def hydra_brute(host, service, user, wordlist):
    print(f"[+] Running Hydra brute force against {host} ({service})")
    subprocess.run(["hydra", "-l", user, "-P", wordlist, host, service])

def sqlmap_attack(url):
    print(f"[+] Running sqlmap on {url}")
    subprocess.run(["sqlmap", "-u", url, "--batch", "--dump"])

# ===============================
# Main
# ===============================
def main():
    parser = argparse.ArgumentParser(description="CTF Multitool")
    subparsers = parser.add_subparsers(dest="module")

    # Port scanner
    scan_parser = subparsers.add_parser("scan", help="Simple port scanner")
    scan_parser.add_argument("--host", required=True)
    scan_parser.add_argument("--ports", default="1-1000")

    # Nmap
    nmap_parser = subparsers.add_parser("nmap", help="Run nmap")
    nmap_parser.add_argument("--target", required=True)

    # Hash
    hash_parser = subparsers.add_parser("hash", help="Hash tools")
    hash_parser.add_argument("action", choices=["gen","crack"])
    hash_parser.add_argument("--type", choices=["md5","sha1","sha256"], default="md5")
    hash_parser.add_argument("--text")
    hash_parser.add_argument("--hash")
    hash_parser.add_argument("--wordlist")

    # Encode/Decode
    b64_parser = subparsers.add_parser("b64", help="Base64 tools")
    b64_parser.add_argument("action", choices=["encode","decode"])
    b64_parser.add_argument("--text", required=True)

    # Gobuster
    gob_parser = subparsers.add_parser("gobuster", help="Gobuster dir scan")
    gob_parser.add_argument("--url", required=True)
    gob_parser.add_argument("--wordlist", required=True)

    # Hydra
    hydra_parser = subparsers.add_parser("hydra", help="Hydra brute force")
    hydra_parser.add_argument("--host", required=True)
    hydra_parser.add_argument("--service", required=True)
    hydra_parser.add_argument("--user", required=True)
    hydra_parser.add_argument("--wordlist", required=True)

    # Sqlmap
    sql_parser = subparsers.add_parser("sqlmap", help="SQLmap attack")
    sql_parser.add_argument("--url", required=True)

    args = parser.parse_args()

    if args.module == "scan":
        port_scan(args.host, args.ports)
    elif args.module == "nmap":
        nmap_scan(args.target)
    elif args.module == "hash":
        if args.action == "gen":
            print(hash_generate(args.text, args.type))
        elif args.action == "crack":
            hash_crack(args.hash, args.type, args.wordlist)
    elif args.module == "b64":
        if args.action == "encode":
            print(encode_b64(args.text))
        else:
            print(decode_b64(args.text))
    elif args.module == "gobuster":
        gobuster_dir(args.url, args.wordlist)
    elif args.module == "hydra":
        hydra_brute(args.host, args.service, args.user, args.wordlist)
    elif args.module == "sqlmap":
        sqlmap_attack(args.url)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
