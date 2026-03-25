import requests
import os
import time

============ COLOR FIX ============

R = '\033[91m'
G = '\033[92m'
Y = '\033[93m'
C = '\033[96m'
W = '\033[97m'
M = '\033[95m'
X = '\033[0m'

================== BANNER ==================

def banner():
os.system("clear || cls")
print(f"""{M}


---

/  _ /  _ / \  / __Y  _ /  _ / \
| | || / ||    \    / \ | / || / || |
| |/|| _/|___ |    | | | _/|| _/|| |/\
_/_/_/    _/ _/_/__/

{C}==================================
 ARIYAN WEB MONITOR 

 Developer : {G}ARIYAN SIAM
 GitHub    : ariyansiampersonal
 Telegram  : @ARIYANSIAM

{X}
""")

================== OPEN LINK ==================

def open_link(url):
try:
os.system(f"termux-open-url {url}")
except:
print(f"{R}Cannot open link!{X}")
time.sleep(1)

================== REQUEST TOOL ==================

def request_tool():
target = input(f"{Y}Enter Target URL: {X}")

try:  
    limit = int(input(f"{Y}How many requests: {X}"))  
except:  
    print(f"{R}Invalid number!{X}")  
    time.sleep(1)  
    return  

print(f"\n{C}Starting requests...\n{X}")  

success = 0  
fail = 0  

for i in range(1, limit + 1):  
    try:  
        r = requests.get(target, timeout=5)  

        if r.status_code == 200:  
            color = G  
            success += 1  
        else:  
            color = R  
            fail += 1  

        print(f"{W}[{i}/{limit}] {C}{target} > {color}{r.status_code}{X}")  

    except Exception as e:  
        print(f"{R}[{i}] Error: {e}{X}")  
        fail += 1  

print(f"\n{C}========== FINAL REPORT =========={X}")  
print(f"{G}Success: {success}{X}")  
print(f"{R}Failed : {fail}{X}")  

input(f"\n{Y}Press Enter to continue...{X}")

================== MAIN ==================

def main():
while True:
banner()
print(f"{W}1. Start Request Test")
print("2. Facebook")
print("3. Telegram")
print("4. GitHub")
print("5. Exit")

choice = input(f"\n{Y}Enter choice: {X}")  

    if choice == '1':  
        request_tool()  
    elif choice == '2':  
        open_link("https://www.facebook.com/FU3K.Y0U")  
    elif choice == '3':  
        open_link("https://t.me/ARIYANSIAM")  
    elif choice == '4':  
        open_link("https://github.com/ariyansiampersonal1999")  
    elif choice == '5':  
        print(f"{G}Goodbye!{X}")  
        break  
    else:  
        print(f"{R}Invalid choice!{X}")  
        time.sleep(1)

if name == "main":
main()
