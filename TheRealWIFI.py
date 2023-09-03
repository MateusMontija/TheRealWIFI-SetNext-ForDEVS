import os
from time import sleep
import requests

sleep(1)

#Animação de carregamento#
print ("\n [___________] 0%")
sleep(0.10);os.system('cls')
print ("\n [██_________] 10%")
sleep(0.10);os.system('cls')
print ("\n [███________] 20%")
sleep(0.10);os.system('cls')
print ("\n [████_______] 30%")
sleep(0.10);os.system('cls')
print ("\n [█████______] 40%")
sleep(0.10);os.system('cls')
print ("\n [██████_____] 50%")
sleep(0.10);os.system('cls')
print ("\n [███████____] 60%")
sleep(0.10);os.system('cls')
print ("\n [████████___] 70%")
sleep(0.10);os.system('cls')
print ("\n [█████████__] 80%")
sleep(0.10);os.system('cls')
print ("\n [██████████_] 90%")
sleep(0.20);os.system('cls')
print ("\n [███████████] 100%")
#Animação de carregamento#

os.system('cls')

print("""
 ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
 ░████████╗██╗░░██╗███████╗░░██████╗░███████╗░█████╗░██╗░░░░░░░░██╗░░░░░░░██╗██╗███████╗██░
 ░╚══██╔══╝██║░░██║██╔════╝░░██╔══██╗██╔════╝██╔══██╗██║░░░░░░░░██║░░██╗░░██║██║██╔════╝██░
 ░░░░██║░░░███████║█████╗░░░░██████╔╝█████╗░░███████║██║░░░░░░░░╚██╗████╗██╔╝██║█████╗░░██░
 ░░░░██║░░░██╔══██║██╔══╝░░░░██╔══██╗██╔══╝░░██╔══██║██║░░░░░░░░░████╔═████║░██║██╔══╝░░██░
 ░░░░██║░░░██║░░██║███████╗░░██║░░██║███████╗██║░░██║███████╗░░░░╚██╔╝░╚██╔╝░██║██║░░░░░██░
 ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░    
 ==========================================================================================
 SetNext(ForDEVS)   <------------------------------------------------------------>   v1.2.0
 ==========================================================================================
 
 ---------------------""")

choose = input(" [1]=[COMEÇAR]\n [2]=[SAIR]\n ---------------------\n ―――>")



def TheRealWIFI():
    print("\n  Verificando...")
    import speedtest


    MyTest = speedtest.Speedtest()


    #<--DOWNLOAD-->#
    downloadSpeed = MyTest.download()
    #<--DOWNLOAD-->#


    #<--UPLOAD-->#
    uploadSpeed = MyTest.upload()
    #<--UPLOAD-->#


    #<--PING-->#
    PING = MyTest.results.ping
    #<--PING-->#


    #<--PublicIP-->#
    publicIP = requests.get('https://api.ipify.org/').text
    #<--PublicIP-->#

    os.system('cls')

    print(f"""
 ▀█▀ █ █ █▀▀  █▀█ █▀▀ █▀█ █    █ █ █ █ █▀▀ █
  █  █▀█ ██▄  █▀▄ ██▄ █▀█ █▄▄  ▀▄▀▄▀ █ █▀  █
 ============================================
 ►PublicIP: {publicIP}        
 ►Download: {downloadSpeed / 10**6:.2f}
 ►Upload: {uploadSpeed / 10**6:.2f}
 ►PING: {PING:.2f}
 ============================================""")
    
    input(" [OK]")
    input(" ")
    exit()


if choose == "1":

    os.system('cls')
    TheRealWIFI()

if choose == "2":

    os.system('cls')
    print("\n  ...")
    exit()


os.system('cls')

print("\n ATENÇÃO[ERRO]!\n ----------------------------\n Abra o programa novamente\n você não digitou 1 e nem 2.")
sleep(4)