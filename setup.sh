#!/bin/bash

# ================= WARNA =================
R="\033[31m"; G="\033[32m"; Y="\033[33m"
B="\033[34m"; P="\033[35m"; C="\033[36m"
W="\033[97m"; N="\033[0m"

clear

# ================= BANNER =================
echo -e "${P}"
cat << "EOF"
╔══════════════════════════════════════╗
║   PYTHON ENCODER AUTO SETUP TOOL     ║
║        by Ruiix_.volt                ║
╚══════════════════════════════════════╝
EOF
echo -e "${N}"

# ================= DETEKSI OS =================
if [[ -d "/data/data/com.termux" ]]; then
    OS="TERMUX"
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    OS="LINUX"
else
    OS="UNKNOWN"
fi

echo -e "${C}[INFO] Detected OS : ${W}$OS${N}"
sleep 1

# ================= PROGRESS =================
progress() {
    for i in {1..25}; do
        echo -ne "${G}█${N}"
        sleep 0.03
    done
    echo
}

# ================= INSTALL PYTHON =================
install_python() {
    echo -e "${B}[+] Installing Python...${N}"
    if [[ "$OS" == "TERMUX" ]]; then
        pkg update -y && pkg install python -y
    elif [[ "$OS" == "LINUX" ]]; then
        sudo apt update -y && sudo apt install python3 python3-pip -y
    fi
}

command -v python3 >/dev/null 2>&1 || install_python
progress

# ================= FIX PIP =================
echo -e "${B}[+] Fixing pip...${N}"
python3 -m ensurepip --default-pip >/dev/null 2>&1 || true
python3 -m pip install --upgrade pip --quiet
progress

# ================= AUTO FIX MODULE ERROR =================
echo -e "${B}[+] Checking required modules...${N}"
python3 - <<EOF
import sys
mods = ["os","sys","base64","zlib","marshal","random","string","hashlib","time"]
missing = []
for m in mods:
    try:
        __import__(m)
    except:
        missing.append(m)

if missing:
    print("Missing modules:", missing)
else:
    print("All required modules OK")
EOF
progress

# ================= DONE =================
echo -e "${G}"
echo "╔══════════════════════════════════════╗"
echo "║      SETUP SUCCESS – READY TO USE    ║"
echo "╚══════════════════════════════════════╝"
echo -e "${N}"

echo -e "${C}[RUN] ${W}python encode.py /path/script.py${N}"
