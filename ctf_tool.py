#!/usr/bin/env python3
# interactive_ctf_tool.py
#
# Interactive CTF Helper Tool
# Javid üçün hazırlanıb :)

import os
import subprocess
import hashlib
import base64

def clear():
    os.system("clear" if os.name == "posix" else "cls")

# ===============================
# 1. Nmap
# ===============================
def nmap_menu():
    clear()
    print("=== Nmap Scanner ===")
    print("1) Quick scan (top 1000 ports)")
    print("2) Service & version detection (-sV)")
    print("3) Stealth scan (-sS)")
    print("4) Full scan (all ports)")
    choice = input("Seçim: ")

    target = input("Hədəf IP/Host daxil et: ")

    if choice == "1":
        cmd = ["nmap", target]
    elif choice == "2":
        cmd = ["nmap", "-sV", target]
    elif choice == "3":
        cmd = ["nmap", "-sS", target]
    elif choice == "4":
        cmd = ["nmap", "-p-", target]
    else:
        print("Yanlış seçim!")
        return

    print(f"[+] Running: {' '.join(cmd)}")
    subprocess.run(cmd)

# ===============================
# 2. Gobuster
# ===============================
def gobuster_menu():
    clear()
    print("=== Gobuster ===")
    url = input("Hədəf URL daxil et (http://ip): ")
    wordlist = input("Wordlist faylının yolunu daxil et: ")

    cmd = ["gobuster", "dir", "-u", url, "-w", wordlist]
    print(f"[+] Running: {' '.join(cmd)}")
    subprocess.run(cmd)

# ===============================
# 3. Hydra
# ===============================
def hydra_menu():
    clear()
    print("=== Hydra Brute Force ===")
    host = input("Hədəf IP: ")
    service = input("Xidmət (ssh, ftp, http, mysql və s.): ")
    user = input("İstifadəçi adı: ")
    wordlist = input("Parol wordlist: ")

    cmd = ["hydra", "-l", user, "-P", wordlist, host, service]
    print(f"[+] Running: {' '.join(cmd)}")
    subprocess.run(cmd)

# ===============================
# 4. SQLmap
# ===============================
def sqlmap_menu():
    clear()
    print("=== SQLmap ===")
    url = input("Hədəf URL (məs: http://ip/vuln.php?id=1): ")

    cmd = ["sqlmap", "-u", url, "--batch", "--dump"]
    print(f"[+] Running: {' '.join(cmd)}")
    subprocess.run(cmd)

# ===============================
# 5. Hash Tools
# ===============================
def hash_menu():
    clear()
    print("=== Hash Tools ===")
    print("1) Hash generate")
    print("2) Hash crack (wordlist ilə)")
    choice = input("Seçim: ")

    algo = input("Hash növü (md5, sha1, sha256): ")

    if choice == "1":
        text = input("Hashlamaq üçün text: ")
        if algo == "md5":
            print(hashlib.md5(text.encode()).hexdigest())
        elif algo == "sha1":
            print(hashlib.sha1(text.encode()).hexdigest())
        elif algo == "sha256":
            print(hashlib.sha256(text.encode()).hexdigest())
    elif choice == "2":
        target_hash = input("Hədəf hash: ")
        wordlist = input("Wordlist faylı: ")
        with open(wordlist, "r", encoding="utf-8", errors="ignore") as f:
            for word in f:
                word = word.strip()
                if algo == "md5":
                    candidate = hashlib.md5(word.encode()).hexdigest()
                elif algo == "sha1":
                    candidate = hashlib.sha1(word.encode()).hexdigest()
                elif algo == "sha256":
                    candidate = hashlib.sha256(word.encode()).hexdigest()
                if candidate == target_hash:
                    print(f"[+] Found: {word}")
                    return
        print("[-] Not found in wordlist.")
    else:
        print("Yanlış seçim!")

# ===============================
# 6. Base64 Tools
# ===============================
def b64_menu():
    clear()
    print("=== Base64 Tools ===")
    print("1) Encode")
    print("2) Decode")
    choice = input("Seçim: ")

    text = input("Mətn: ")

    if choice == "1":
        print(base64.b64encode(text.encode()).decode())
    elif choice == "2":
        print(base64.b64decode(text).decode())

# ===============================
# MAIN MENU
# ===============================
def main():
    while True:
        clear()
        print("===== CTF Interactive Tool =====")
        print("1) Nmap")
        print("2) Gobuster")
        print("3) Hydra")
        print("4) SQLmap")
        print("5) Hash Tools")
        print("6) Base64 Tools")
        print("0) Çıxış")
        choice = input("Seçim: ")

        if choice == "1":
            nmap_menu()
        elif choice == "2":
            gobuster_menu()
        elif choice == "3":
            hydra_menu()
        elif choice == "4":
            sqlmap_menu()
        elif choice == "5":
            hash_menu()
        elif choice == "6":
            b64_menu()
        elif choice == "0":
            print("Çıxış...")
            break
        else:
            print("Yanlış seçim!")

        input("\n[ENTER] bas davam etmək üçün...")

if __name__ == "__main__":
    main()
