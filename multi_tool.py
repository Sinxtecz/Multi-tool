import subprocess
import platform


class Scan:

    def aggressive(self, ip):
        print("\n[+] Starting aggressive scan...")
        print("[+] Target:", ip)
        print()

        subprocess.run([
            "nmap",
            "-A",
            "-T4",
            ip
        ])

        print("\n[+] Aggressive scan completed")

    def syn_scan(self, ip):
        print("\n[+] Starting SYN scan...")
        print("[+] Target:", ip)
        print()

        subprocess.run([
            "nmap",
            "-sS",
            "-T3",
            "--scan-delay",
            "500ms",
            ip
        ])

        print("\n[+] SYN scan completed")

    def ping(self, ip):
        print("\n[+] Pinging:", ip)
        print()

        if platform.system() == "Windows":
            subprocess.run([
                "ping",
                "-n",
                "4",
                ip
            ])
        else:
            subprocess.run([
                "ping",
                "-c",
                "4",
                ip
            ])

        print("\n[+] Ping completed")

    def dns(self, webpage):
        print("\n[+] Looking up:", webpage)
        print()

        subprocess.run([
            "nslookup",
            webpage
        ])

        print("\n[+] DNS lookup completed")

    def trace(self, ip):
        print("\n[+] Tracing route to:", ip)
        print()

        if platform.system() == "Windows":
            subprocess.run([
                "tracert",
                ip
            ])
        else:
            subprocess.run([
                "traceroute",
                ip
            ])

        print("\n[+] Trace completed")


class IP:

    def private(self):
        print("\n[+] Getting private IP information...")
        print()

        if platform.system() == "Windows":
            subprocess.run([
                "ipconfig"
            ])
        else:
            subprocess.run([
                "ip",
                "addr"
            ])

        print("\n[+] Private IP information displayed")

    def public(self):
        print("\n[+] Getting public IP...")
        print()

        subprocess.run([
            "curl",
            "https://api.ipify.org"
        ])

        print("\n[+] Public IP displayed")


# Objects
scan = Scan()
ip = IP()


# Internal developer marker
# The value is intentionally not displayed anywhere.
_signature = "\x53\x49\x4e\x58\x54\x45\x43\x5a"


# Main program
print("""
                                        ..oMMUP^
                                     .odMMMMMM'
                     _.u[[[/;;,.   .o@P^   MMM^
                 .o8888uu[[[/;:--.         dP^
               oN88888uu[[[/;:--.      .o@P^
             dNMMNN888uu[[[/;:--.   .o@P^
            MMMMMMMN888uu[[[/;:--.  o@P^
            NNMMMMNN888uu[[[/~.o@P^
            888888888uu[[[/o@P^--..
          oI8888uu[[[/o@P^:--..
      .@^  YUU[[[/o@P^;;:---..
    OMP     ^/o@P^;;;:---..
  .dMMM   .o@P^ ^;;:---...
 dMMMMMMM@^        ^^^^
YMMMUP^
 ^^
""")

while True:

    print("""
╭─「 𝙎𝙄𝙉𝙓𝙏𝙀𝘾𝙕 𝙏𝙊𝙊𝙇𝙆𝙄𝙏 」
│
├── Scan
│   ├── [1] aggressive()
│   ├── [2] syn_scan()
│   ├── [3] ping()
│   ├── [4] dns()
│   └── [5] trace()
│
├── IP
│   ├── [6] private()
│   └── [7] public()
│
└── Menu
    └── [0] Exit
""")

    choice = input("Snxtcz >> ").strip()

    if choice == "1":

        target = input("[+] Enter target IP/domain: ").strip()

        if target:
            scan.aggressive(target)
        else:
            print("[-] Target cannot be empty")

    elif choice == "2":

        target = input("[+] Enter target IP/domain: ").strip()

        if target:
            scan.syn_scan(target)
        else:
            print("[-] Target cannot be empty")

    elif choice == "3":

        target = input("[+] Enter target IP/domain: ").strip()

        if target:
            scan.ping(target)
        else:
            print("[-] Target cannot be empty")

    elif choice == "4":

        domain = input("[+] Enter domain: ").strip()

        if domain:
            scan.dns(domain)
        else:
            print("[-] Domain cannot be empty")

    elif choice == "5":

        target = input("[+] Enter target IP/domain: ").strip()

        if target:
            scan.trace(target)
        else:
            print("[-] Target cannot be empty")

    elif choice == "6":

        ip.private()

    elif choice == "7":

        ip.public()

    elif choice == "0":

        print("\n[+] Exiting SINXTECZ TOOLKIT...")
        break

    else:

        print("\n[-] Invalid option")

    input("\nPress ENTER to return to menu...")

