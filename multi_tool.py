import platform
import subprocess


print("""
╔══════════════════════════════════════╗
║          S I N X T E C Z             ║
║       Python Security Tool           ║
╚══════════════════════════════════════╝

[+] Version: 1.0
[+] Type "help" to see the menu
""")


while True:

    command = input("Snxtcz >> ").strip().lower()

    # show menu
    if command == "help":
        print("""
[+] MENU

[1] Ping
[2] DNS Lookup
[3] Nmap Scan
[0] Exit
""")

    # ping
    elif command == "1":

        target = input("[+] Enter IP/Domain: ")

        print("\n[+] Pinging", target, "...\n")

        if platform.system() == "Windows":
            subprocess.run(["ping", "-n", "4", target])
        else:
            subprocess.run(["ping", "-c", "4", target])

    # dns lookup
    elif command == "2":

        target = input("[+] Enter Domain/IP: ")

        print("\n[+] Looking up", target, "...\n")

        subprocess.run(["nslookup", target])

    # nmap
    elif command == "3":

        target = input("[+] Enter Target IP/Domain: ")

        print("\n[+] Starting Nmap scan...")
        print("[+] Target:", target)
        print("[!] This might take a little while.\n")

        subprocess.run([
            "nmap",
            "-F",
            "-T4",
            "-sV",
            target
        ])

    # exit
    elif command == "0":

        print("\n[+] Closing Sinxtecz...")
        break

    else:

        print("[-] Unknown command. Type 'help'.")
