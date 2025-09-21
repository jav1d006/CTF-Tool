#!/usr/bin/env python3
# interactive_ctf_tool.py
#
# Interactive CTF Helper Tool
# Javid üçün hazırlanıb :)

import os
import subprocess
import hashlib
import base64
import time

def clear():
    os.system("clear" if os.name == "posix" else "cls")

# ===============================
# 1. Nmap
# ===============================
def nmap_advanced_menu():
    while True:
        print("\n--- Nmap Geniş Menyu ---")
        print("1-         Aktiv host / Şəbəkə aşkarlanması (-sn)")
        print("2-         Bütün portları skan et (-p-)")
        print("3-         Xidmət və versiya aşkarlanması (-sV)")
        print("4-         Default scriptlər ilə (-sC)")
        print("5-         Aqressiv skan (-A)")
        print("6-         Aqressiv + OS aşkarlanması + zəiflik scriptləri (-A -O -T4 --script=vuln)")
        print("7-         Versiya + scriptlər + 5000pps + bütün portlar (-sV -sC -T4 --min-rate 5000 -p-)")
        print("8-         Xüsusi Nmap əmri")
        print("9-         Nmap menyusundan çıx")

        secim = input("Seçiminizi daxil edin: ")

        if secim == "1":
            target = input("Hədəf IP/Domen: ")
            os.system(f"sudo nmap -sn {target}")

        elif secim == "2":
            target = input("Hədəf IP/Domen: ")
            os.system(f"sudo nmap -p- {target}")

        elif secim == "3":
            target = input("Hədəf IP/Domen: ")
            os.system(f"sudo nmap -sV {target}")

        elif secim == "4":
            target = input("Hədəf IP/Domen: ")
            os.system(f"sudo nmap -sC {target}")

        elif secim == "5":
            target = input("Hədəf IP/Domen: ")
            os.system(f"nmap -A {target}")

        elif secim == "6":
            target = input("Hədəf IP/Domen: ")
            os.system(f"nmap -A -O -T4 --script=vuln {target}")

        elif secim == "7":
            target = input("Hədəf IP/Domen: ")
            os.system(f"nmap -sV -sC -T4 --min-rate 5000 -p- {target}")

        elif secim == "8":
            target = input("Hədəf IP/Domen: ")
            params = input("Əlavə parametrləri daxil et: ")
            os.system(f"nmap {params} {target}")

        elif secim == "9":
            print("Nmap menyusundan çıxılır...")
            break

        else:
            print("Yanlış seçim! Təkrar yoxlayın.")

# ===============================
# 2. Gobuster
# ===============================
def gobuster_menu():
    wordlists = {
        "1": "/Desktop/CTF-Tool/src/wordlist/common.txt",
        "2": "/Desktop/CTF-Tool/src/wordlist/directory-list-1.0.txt",
        "3": "/Desktop/CTF-Tool/src/wordlist/directory-list-2.3-small.txt",
        "4": "/Desktop/CTF-Tool/src/wordlist/directory-list-2.3-medium.txt",
        "5": "/Desktop/CTF-Tool/src/wordlist/directory-list-lowercase-2.3-small.txt",
        "6": "/Desktop/CTF-Tool/src/wordlist/directory-list-lowercase-2.3-medium.txt",
        "7": "/Desktop/CTF-Tool/src/wordlist/medium.txt",
        "8": "/Desktop/CTF-Tool/src/wordlist/names.txt",
        "9": "/Desktop/CTF-Tool/src/wordlist/password.txt",
        "10": "/Desktop/CTF-Tool/src/wordlist/jav1d006"
    }

    while True:
        print("\n--- Gobuster Menyu ---")
        print("1-         Directory / File Brute Force (dir)")
        print("2-         Virtual Host Brute Force (vhost)")
        print("3-         DNS Subdomain Brute Force (dns)")
        print("4-         Custom Gobuster əmri")
        print("5-         Gobuster menyusundan çıx")

        secim = input("Seçiminizi daxil edin: ")

        if secim in ["1", "2", "3"]:
            url_or_domain = input("Hədəf URL/Domen: ")
            print("\nWordlist şablonunu seçin:")
            for key, wl in wordlists.items():
                print(f"{key}) {wl.split('/')[-1]}")
            wl_choice = input("Seçim: ")

            wordlist = wordlists.get(wl_choice, "/Desktop/CTF-Tool/src/wordlist/common.txt")

            if secim == "1":
                os.system(f"gobuster dir -u {url_or_domain} -w {wordlist} -t 50")
            elif secim == "2":
                os.system(f"gobuster vhost -u {url_or_domain} -w {wordlist} -t 50")
            elif secim == "3":
                os.system(f"gobuster dns -d {url_or_domain} -w {wordlist} -t 50")

        elif secim == "4":
            cmd = input("Tam Gobuster əmri daxil edin: ")
            os.system(f"gobuster {cmd}")

        elif secim == "5":
            print("Gobuster menyusundan çıxılır...")
            break

        else:
            print("Yanlış seçim! Təkrar yoxlayın.")

# ===============================
# 3. Hydra
# ===============================
def hydra_menu():
    wordlists = {
        "1": "/Desktop/CTF-Tool/src/wordlist/rockyou.txt",
        "2": "/Desktop/CTF-Tool/src/wordlist/fasttrack.txt",
        "3": "/Desktop/CTF-Tool/src/wordlist/common.txt",
        "4": "/Desktop/CTF-Tool/src/wordlist/passwords.txt",
        "5": "/Desktop/CTF-Tool/src/wordlist/jav1d006"
    }

    while True:
        print("\n--- Hydra Menyu ---")
        print("1-         SSH")
        print("2-         FTP")
        print("3-         HTTP-Form (web login)")
        print("4-         MySQL")
        print("5-         Custom Hydra əmri")
        print("6-         Hydra menyusundan çıx")

        secim = input("Seçiminizi daxil edin: ")

        if secim in ["1","2","3","4"]:
            host = input("Hədəf IP/Domen: ")

            print("\nWordlist şablonunu seçin:")
            for key, wl in wordlists.items():
                print(f"{key}) {wl.split('/')[-1]}")
            wl_choice = input("Seçim: ")
            wordlist = wordlists.get(wl_choice, "/Desktop/CTF-Tool/src/wordlist/rockyou.txt")

            if secim == "1":  # SSH
                user = input("İstifadəçi adı: ")
                os.system(f"hydra -l {user} -P {wordlist} {host} ssh")

            elif secim == "2":  # FTP
                user = input("İstifadəçi adı: ")
                os.system(f"hydra -l {user} -P {wordlist} {host} ftp")

            elif secim == "3":  # HTTP-Form
                url = input("Form URL (məs: http://site.com/login.php): ")
                user = input("İstifadəçi adı: ")
                password_field = input("Password field adı (məs: password): ")
                os.system(f"hydra -l {user} -P {wordlist} {url} http-post-form \"{url}:{user}=^USER^&{password_field}=^PASS^:F=incorrect\"")

            elif secim == "4":  # MySQL
                user = input("İstifadəçi adı: ")
                os.system(f"hydra -l {user} -P {wordlist} {host} mysql")

        elif secim == "5":
            cmd = input("Tam Hydra əmri daxil edin: ")
            os.system(f"hydra {cmd}")

        elif secim == "6":
            print("Hydra menyusundan çıxılır...")
            break

        else:
            print("Yanlış seçim! Təkrar yoxlayın.")

# ===============================
# 4. SQLmap
# ===============================
def sqlmap_menu():
    wordlists = {
        "1": "/Desktop/CTF-Tool/src/wordlist/rockyou.txt",
        "2": "/Desktop/CTF-Tool/src/wordlist/fasttrack.txt",
        "3": "/Desktop/CTF-Tool/src/wordlist/common.txt",
        "4": "/Desktop/CTF-Tool/src/wordlist/passwords.txt"
    }

    while True:
        print("\n--- SQLmap Menyu ---")
        print("1-         Basic URL Scan")
        print("2-         Crawl & Scan")
        print("3-         Database Dump")
        print("4-         Use Wordlist (login/password)")
        print("5-         Custom SQLmap command")
        print("6-         SQLmap menyusundan çıx")

        secim = input("Seçiminizi daxil edin: ")

        if secim == "1":
            url = input("Target URL (məs: http://site.com/vuln.php?id=1): ")
            os.system(f"sqlmap -u \"{url}\" --batch")

        elif secim == "2":
            url = input("Target URL: ")
            os.system(f"sqlmap -u \"{url}\" --crawl=2 --batch")

        elif secim == "3":
            url = input("Target URL: ")
            os.system(f"sqlmap -u \"{url}\" --dump --batch")

        elif secim == "4":
            url = input("Target URL: ")
            print("\nWordlist şablonunu seçin:")
            for key, wl in wordlists.items():
                print(f"{key}) {wl.split('/')[-1]}")
            wl_choice = input("Seçim: ")
            wordlist = wordlists.get(wl_choice, "CTF-Tool/src/wordlist/rockyou.txt")
            os.system(f"sqlmap -u \"{url}\" --passwords -P {wordlist} --batch")

        elif secim == "5":
            cmd = input("Tam SQLmap əmri daxil edin: ")
            os.system(f"sqlmap {cmd}")

        elif secim == "6":
            print("SQLmap menyusundan çıxılır...")
            break

        else:
            print("Yanlış seçim! Təkrar yoxlayın.")

# ===============================
# 5. Hash Tools
# ===============================
def hash_tools_menu():
    while True:
        print("\n--- Hash Tools Menyu ---")
        print("1-         MD5")
        print("2-         SHA1")
        print("3-         SHA256")
        print("4-         NTLM")
        print("5-         Custom Hash")
        print("6-         Hash Tools menyusundan çıx")

        secim = input("Seçiminizi daxil edin: ")

        if secim in ["1","2","3","4"]:
            data = input("Hash-lanacaq mətn və ya parol: ").encode()

            if secim == "1":
                result = hashlib.md5(data).hexdigest()
            elif secim == "2":
                result = hashlib.sha1(data).hexdigest()
            elif secim == "3":
                result = hashlib.sha256(data).hexdigest()
            elif secim == "4":
                import binascii
                result = hashlib.new('md4', data.decode('utf-8').encode('utf-16le')).hexdigest()

            print(f"\nNəticə: {result}")

        elif secim == "5":
            algo = input("Hash alqoritmi adı (məs: sha512, sha3_256): ")
            try:
                h = hashlib.new(algo)
                data = input("Hash-lanacaq mətn və ya parol: ").encode()
                h.update(data)
                print(f"\nNəticə: {h.hexdigest()}")
            except:
                print("Yanlış alqoritm adı!")

        elif secim == "6":
            print("Hash Tools menyusundan çıxılır...")
            break

        else:
            print("Yanlış seçim! Təkrar yoxlayın.")

# ===============================
# 6. Base64 Tools
# ===============================
def base64_tools_menu():
    while True:
        print("\n--- Base64 Alətləri Menyu ---")
        print("1-         Mətn Encode")
        print("2-         Mətn Decode")
        print("3-         Fayl Encode")
        print("4-         Fayl Decode")
        print("5-         Base64 menyusundan çıx")

        secim = input("Seçiminizi daxil edin: ")

        if secim == "1":
            text = input("Encode olunacaq mətn: ").encode()
            encoded = base64.b64encode(text)
            print(f"\nNəticə: {encoded.decode()}")

        elif secim == "2":
            text = input("Decode olunacaq Base64 mətn: ").encode()
            try:
                decoded = base64.b64decode(text)
                print(f"\nNəticə: {decoded.decode()}")
            except Exception as e:
                print(f"Xəta: {e}")

        elif secim == "3":
            file_path = input("Encode olunacaq faylın yolu: ")
            try:
                with open(file_path, "rb") as f:
                    encoded = base64.b64encode(f.read())
                print(f"\nNəticə:\n{encoded.decode()}")
            except Exception as e:
                print(f"Xəta: {e}")

        elif secim == "4":
            file_path = input("Decode olunacaq Base64 faylın yolu: ")
            try:
                with open(file_path, "rb") as f:
                    decoded = base64.b64decode(f.read())
                print("\nDecoded content:")
                print(decoded.decode(errors='ignore'))
            except Exception as e:
                print(f"Xəta: {e}")

        elif secim == "5":
            print("Base64 menyusundan çıxılır...")
            break

        else:
            print("Yanlış seçim! Təkrar yoxlayın.")

# ===============================
# MAIN MENU
# ===============================
from colorama import init, Fore, Style

init(autoreset=True)

def clear():
    os.system("clear" if os.name == "posix" else "cls")

def show_banner():
    banner_lines = [
        "████████████████████████████████████████",
        "█                                      █",
        "█       J A V I D   C Y B E R          █",
        "█   Interactive CTF & Pentest Tool     █",
        "█                                      █",
        "████████████████████████████████████████",
    ]
    for line in banner_lines:
        print(Fore.CYAN + Style.BRIGHT + line)
        time.sleep(0.1)  # Animasiya effekti
    print("\n")

def main():
    while True:
        clear()
        show_banner()
        
        print(Fore.YELLOW + "┌───────────── TOOLS ──────────────┐")
        print(Fore.GREEN + "│ 1) Nmap                          │")
        print(Fore.GREEN + "│ 2) Gobuster                      │")
        print(Fore.GREEN + "│ 3) Hydra                         │")
        print(Fore.GREEN + "│ 4) SQLmap                        │")
        print(Fore.GREEN + "│ 5) Hash Tools                     │")
        print(Fore.GREEN + "│ 6) Base64 Tools                   │")
        print(Fore.RED   + "│ 0) Çıxış                         │")
        print(Fore.YELLOW + "└──────────────────────────────────┘\n")

        choice = input(Fore.CYAN + "Seçiminizi daxil edin: ")

        if choice == "1":
            nmap_advanced_menu()
        elif choice == "2":
            gobuster_menu()
        elif choice == "3":
            hydra_menu()
        elif choice == "4":
            sqlmap_menu()
        elif choice == "5":
            hash_tools_menu()
        elif choice == "6":
            base64_tools_menu()
        elif choice == "0":
            print(Fore.RED + "Çıxış...")
            break
        else:
            print(Fore.RED + "Yanlış seçim!")

        input(Fore.MAGENTA + "\n[ENTER] bas davam etmək üçün...")

if __name__ == "__main__":
    main()

       
