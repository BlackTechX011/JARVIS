# JARVIS by BlackTechX

import http.server
import socketserver
import os
import sys
from colorama import init, Fore, Style
import time
import webbrowser

def clear():
    _ = os.system('cls' if os.name == 'nt' else 'clear')
    
def Type(data):
    print(Fore.LIGHTBLUE_EX + "└─ " + "\033[1;37m" + data)

def write(data):
    for char in data:
        sys.stdout.write(Fore.LIGHTCYAN_EX + char)
        sys.stdout.flush()
        time.sleep(0.02) 
    print()
    
    
def open_browser(url):
    try:
        webbrowser.open(url)
    except Exception as e:
        print(f"Error opening browser: {e}")
def JARVIS():
    print(Fore.LIGHTBLUE_EX + """     
     ____.  _____  ______________   ____.___  _________
    |    | /  _  \ \______   \   \ /   /|   |/   _____/
    |    |/  /_\  \ |       _/\   Y   / |   |\_____  \ 
/\__|    /    |    \|    |   \ \     /  |   |/        \ 
\________\____|__  /|____|_  /  \___/   |___/_______  /
                 \/        \/                       \/ 
Virtual Assistant JARVIS By BlackTechX
""")
    
DIRECTORY = './'
PORT = 8001


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass

with socketserver.TCPServer(("", PORT), QuietHandler) as httpd:
    clear()
    JARVIS()
    write("JARVIS is ready. Visit:")
    write(f"http://localhost:{PORT}")
    time.sleep(2)
    open_browser(f"http://localhost:{PORT}")
    
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped by user.")
