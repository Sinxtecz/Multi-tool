import platform
import subprocess

print(r"""
 ███████╗██╗███╗   ██╗██╗  ██╗████████╗███████╗ ██████╗███████╗
 ██╔════╝██║████╗  ██║╚██╗██╔╝╚══██╔══╝██╔════╝██╔════╝╚══███╔╝
 ███████╗██║██╔██╗ ██║ ╚███╔╝    ██║   █████╗  ██║        ███╔╝
 ╚════██║██║██║╚██╗██║ ██╔██╗    ██║   ██╔══╝  ██║       ███╔╝
 ███████║██║██║ ╚████║██╔╝ ██╗   ██║   ███████╗╚██████╗ ███████╗
 ╚══════╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝   ╚═╝   ╚══════╝ ╚═════╝ ╚══════╝

       ╔══════════════════════════════════════════════════════╗
       ║              S I N X T E C Z   C Y B E R             ║
       ║                  P Y T H O N   T O O L               ║
       ╠══════════════════════════════════════════════════════╣
       ║                                                      ║
       ║   [ Framework ]   Network Reconnaissance             ║
       ║   [ Version   ]   1.1.0                                ║
       ║   [ Engine    ]   Python + System Tools              ║
       ║   [ Interface ]   Interactive CLI                    ║
       ║                                                      ║
       ╚══════════════════════════════════════════════════════╝

        ┌─[ SYSTEM ]
        │
        ├── Platform      : Python Security Toolkit
        ├── Purpose       : Network Reconnaissance
        ├── Interface     : Interactive Terminal
        └── Status        : ONLINE
       
        ┌─[ MODULES ]
        │
        ├── [01] ICMP / Ping
        ├── [02] DNS Lookup
        ├── [03] Nmap Aggressive Scan
        ├── [04] Nmap SYN Scan
        ├── [05] YOUR IP ADDRESS
        │     ├──(5.1) PRIVATE IP ADDRESS.
        │     └──(5.2) PUBLIC IP ADDRESS.
        └── [06] TRACE ROUTE
        
        
        ┌─[ COMMANDS ]
        │
        ├── help          → Display available commands
        ├── 1-6           → Select a module
        └── 0             → Exit framework

        ┌─[ NOTICE ]
        │
        └── Use only on systems you own or are authorized to test.

        ══════════════════════════════════════════════════════


""")


while True:

    command = input("Snxtcz >> ").strip().lower()

    # show menu
    if command == "help":
        print("""
[+] MENU

[1] Ping
 ╰─> Check if a target is online.

[2] DNS Lookup
 ╰─> Find a domain's IP and DNS information.

[3] Nmap Scan (Aggressive)
 ╰─> Detailed scan for ports, services, and versions.
     Use for deeper network reconnaissance.

[4] Nmap Scan (Stealthy)
 ╰─> Quieter scan to find open ports.
     Use for basic port reconnaissance.
     
 [5] IP Information
 ╰─> Display your private and public IP addresses.
     Use this to identify your local and internet-facing addresses.
     
 [6] Traceroute
╰─> Show the network path packets take to reach a target.
    Use this to understand where traffic travels and find network delays.

[0] Exit
 ╰─> Close the toolkit.
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
            "-A",
            "-O",
            target
        ])
    elif command == "4":
        target = input("[+] Enter Target IP/Domain: ")
        print("\n[+] Starting Nmap scan...")
        print("[+] This may take time because of the stealth, that we don't sacrifice.")
        print(".")
        subprocess.run(["nmap",
                        "-sS",
                        "-T3",
                        "--scan-delay",
                        "500ms",
                        target])
    elif command == "5":
        print("Please choose between 5.1 and 5.2.")

    elif command == "5.1":
        if platform.system() == "Windows":
            subprocess.run(["ipconfig"])
        else:
            subprocess.run(["ip addr"])

    elif command == "5.2":
        if platform.system() == "Windows":
            subprocess.run(["curl","https://api.ipify.org"])
        else:
            subprocess.run(["curl", "https://api.ipify.org"])

    elif command == "6":
        target = input("\n[+] Enter Target IP/Domain: ")

        if platform.system() == "Windows":
            subprocess.run(["tracert",
                            target])
        else:
            subprocess.run(["traceroute",
                            target])

    # exit
    elif command == "0":

        print("\n[+] Closing Sinxtecz...")
        break

    else:

        print("[-] Unknown command. Type 'help'.")
