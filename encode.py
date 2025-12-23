import os, time, sys, base64, zlib, marshal, random, string, hashlib

# clear
os.system("cls" if os.name == "nt" else "clear")

def rand(n=8):
    return ''.join(random.choice(string.ascii_letters) for _ in range(n))

def xor(data, key):
    return bytes(b ^ key[i % len(key)] for i, b in enumerate(data))

def kdf():
    seed = f"{os.getpid()}{random.random()}".encode()
    return hashlib.sha256(seed).digest()

# ================= PYTHON HIGH =================
def encode_python(file):
    if not os.path.isfile(file):
        print(f"File not found ✖: {file}")
        return

    src = open(file, "rb").read()
    code = compile(src, "<secure>", "exec")

    m = marshal.dumps(marshal.dumps(code))
    c = zlib.compress(zlib.compress(m, 9), 9)

    key = kdf()
    khex = key.hex()

    x = xor(xor(c, key), key[::-1])
    b64 = base64.b64encode(x).decode()

    parts = [(i, b64[i:i+90]) for i in range(0, len(b64), 90)]
    random.shuffle(parts)

    a,b,c,d,e,f = [rand() for _ in range(6)]

    output = f'''# encoded by Ruiix_.volt
import base64,zlib,marshal
KEY = bytes.fromhex("{khex}")

def _x(d,k):
    return bytes(b^k[i%len(k)] for i,b in enumerate(d))

{a}={parts}
{b}="".join(p[1] for p in sorted({a}))
{b}+="=" * (-len({b}) % 4)
{c}=base64.b64decode({b})
{d}=_x(_x({c},KEY[::-1]),KEY)
{e}=zlib.decompress(zlib.decompress({d}))
{f}=marshal.loads(marshal.loads({e}))
exec({f})
'''
    open(file, "w").write(output)
    print(f"\033[37m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣤⣤⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print(f"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣿⣿⣿⣿⠿⠿⠿⠿⣿⣿⣿⣿⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print(f"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣶⣿⣿⡿⠛⠉⠁⠀⢀⣀⣀⢀⠀⠈⠉⠛⢿⣿⣿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print(f"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⡿⠋⠁⢀⣠⣴⣶⣾⣿⣿⣾⣶⣦⣄⡀⠈⠙⢿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀")
    print(f"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⠏⠀⢀⣴⣿⣿⡿⠟⠛⠋⠙⠛⠛⠿⣿⣿⣦⡀⠀⠹⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀")
    print(f"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⠏⠀⢠⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣄⠀⠸⣿⣿⣇⠀⠀⠀⠀⠀⠀")
    print(f"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡏⠀⢠⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⡆⠀⢹⣿⣿⠀⠀⠀⠀⠀⠀")
    print(f"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⡇⠀⣸⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣇⠀⢸⣿⣿⡇⠀⠀⠀⠀⠀")
    print(f"⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣸⣿⣿⣇⣀⣻⣿⣿⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣿⣿⣿⣀⣸⣿⣿⣇⡀⠀⠀⠀⠀")
    print(f"\033[33m⠀⠀⠀⠀⠀⠀⠀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⠀⠀")
    print(f"⠀⠀⠀⠀⠀⠀⣼⣿⣿⠋⣁⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣌⠙⣿⣿⣧⠀")
    print(f"⠀⠀⠀⠀⠀⢸⡿⠿⠧⠼⠿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠿⠧⠼⠿⣿⡇")
    print(f"⠀⠀⠀⠀⠀⢿⣅⣀⣀⣀⣀⣀⣀⣀⣨⣿⣿⣿⣿⡿⠛⠉⠁⠀⠀⡀⠀⠈⠉⠛⢿⣿⣿⣿⣿⣇⣀⣀⣀⣀⣀⣀⣀⣨⡿")
    print(f"⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⠁⢀⣠⣴⣶⣶⣷⣶⣦⣄⡀⠈⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇")
    print(f"⠀⠀⠀⠀⠀⣾⡏⠉⠉⠉⠉⢹⣿⣿⣿⣿⡟⠁⢀⣴⣿⡿⠟⠛⠉⠉⠙⠻⢿⣿⣦⡀⠈⢻⣿⣿⣿⣿⡏⠉⠉⠉⠉⠹⣷")
    print(f"⠀⠀⠀⠀⠀⢹⣷⣶⣶⣶⣶⣾⣿⣿⣿⡿⠁⠀⣾⣿⡟⠀⠀⣤⣶⣶⣤⠀⠀⠻⣿⣷⡀⠀⢿⣿⣿⣿⣷⣶⣶⣶⣶⣾⡏")
    print(f"⠀⠀⠀⠀⠀⣼⡟⠛⠛⠛⠛⢻⣿⣿⣿⡇⠀⢸⣿⣿⠀⠀⢸⣿⣿⣿⣿⡇⠀⠀⢻⣿⡇⠀⢸⣿⣿⣿⡟⠛⠛⠛⠛⠻⣧")
    print(f"⠀⠀⠀⠀⠀⢻⣧⣤⣤⣤⣤⣼⣿⣿⣿⡇⠀⢸⣿⣿⠀⠀⠀⣿⣿⣿⣿⠀⠀⠀⣾⣿⡇⠀⢸⣿⣿⣿⣧⣤⣤⣤⣤⣼⡟")
    print(f"⠀⠀⠀⠀⠀⣸⡿⠿⠿⠿⠿⢿⣿⣿⣿⣿⡀⠀⢻⣿⣧⠀⢰⣿⡏⢹⣿⡆⠀⣼⣿⡟⠀⢀⣾⣿⣿⣿⡿⠿⠿⠿⠿⢿⣇")
    print(f"⠀⠀⠀⠀⠀⢿⣦⣀⣀⣀⣀⣼⣿⣿⣿⣿⣷⡀⠀⠻⠏⠀⣾⣿⣁⣀⣿⣷⠀⠹⠟⠀⢀⣾⣿⣿⣿⣿⣧⣀⣀⣀⣀⣴⡿")
    print(f"⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠛⠿⠿⠿⠿⠛⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇")
    print(f"⠀⠀⠀⠀⠀⢿⣅⡀⡀⣀⠀⣀⠀⣀⣨⣿⣿⣿⣿⣿⣷⣦⣤⣀⣀⣀⣀⣤⣴⣾⣿⣿⣿⣿⣿⣅⡀⣀⠀⣀⠀⣀⢀⣨⡿")
    print(f"⠀⠀⠀⠀⠀⠘⣿⣿⣯⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⣹⣿⣿⠃")
    print(f"⠀⠀⠀⠀⠀⠀⢻⣿⣿⣄⡻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⣡⣿⣿⡟⠀")
    print(f"⠀⠀⠀⠀⠀⠀⠀⠻⢿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⡿⠟⠀⠀")
    print(f"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠉⠀⠀⠀⠀")
    print("")
    print(f"\033[35m             Developer: Ruiix_.volt")
    print(f"\033[35m           Lock your tools for safety")
    print("")
    time.sleep(1)
    print(f"\033[94m[\033[32mINFO\033[34m] \033[35mFound file      > encode.py")
    time.sleep(2)
    print(f"\033[94m[\033[32mINFO\033[34m] \033[35mLocking process \033[32m• \033[31m• \033[33m•")
    time.sleep(3)
    print(f"\033[94m[\033[32mINFO\033[34m] \033[35mSuccess locking > encode.py")
    print(f"\033[94m[\033[32mINFO\033[34m] \033[35mPath your file > {file}")
    print(f"\033[94m[\033[32mINFO\033[34m] \033[35mYour script has been encoded 9 layers")
# ================= MAIN =================
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} /path/to/script.py")
        sys.exit(1)
    encode_python(sys.argv[1])
