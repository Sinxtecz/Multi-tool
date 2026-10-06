# 𝙎𝙄𝙉𝙓𝙏𝙀𝘾𝙕 TOOLKIT

```text
╭─「 𝙎𝙄𝙉𝙓𝙏𝙀𝘾𝙕 」
╰─┤ CYBER TOOLKIT
```

A lightweight Python networking toolkit built for **learning, practice, and understanding networking tools from the command line.**

## ⚡ Features

* 🔎 Aggressive Nmap Scan
* 🛡️ SYN Scan
* 📡 Ping
* 🌐 DNS Lookup
* 🛣️ Traceroute
* 🖥️ Private IP Information
* 🌍 Public IP Detection
* 🪟 Windows + 🐧 Linux support

---

## 🛠️ Requirements

* Python 3
* Nmap
* cURL
* DNS utilities
* Traceroute utilities

Python's `subprocess` and `platform` modules are built-in, so **no `pip install` is required.**

---

## 🪟 Windows Setup

### 1. Install Python

Download Python 3 from:

https://www.python.org/downloads/

During installation, make sure:

```text
☑ Add Python to PATH
```

Check:

```powershell
python --version
```

### 2. Install Nmap

Download Nmap from:

https://nmap.org/download.html

Check:

```powershell
nmap --version
```

### 3. cURL

Modern Windows versions normally include cURL.

Check:

```powershell
curl --version
```

### 4. Run the toolkit

```powershell
python multi_tool.py
```

---

## 🐧 Linux Setup

### Debian / Ubuntu / Kali

```bash
sudo apt update
sudo apt install python3 nmap curl traceroute
```

Check:

```bash
python3 --version
nmap --version
curl --version
traceroute --version
```

Run:

```bash
python3 multi_tool.py
```

### Arch Linux

```bash
sudo pacman -S python nmap curl traceroute
```

Run:

```bash
python multi_tool.py
```

---

## 📂 Structure

```text
SINXTECZ TOOLKIT
│
├── Scan
│   ├── aggressive()
│   ├── syn_scan()
│   ├── ping()
│   ├── dns()
│   └── trace()
│
├── IP
│   ├── private()
│   └── public()
│
└── Menu
```

## 🎯 Purpose

Built to practice **Python, networking, subprocesses, Linux/Windows commands, and cybersecurity fundamentals**.

> ⚠️ Only scan systems and networks you own or have explicit permission to test.

```text
// crafted by 𝙎𝙄𝙉𝙓𝙏𝙀𝘾𝙕
```
