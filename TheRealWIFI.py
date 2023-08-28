import os
from time import sleep



print("""
 ████████╗██╗░░██╗███████╗  ██████╗░███████╗░█████╗░██╗░░░░░  ░██╗░░░░░░░██╗██╗███████╗██╗
 ╚══██╔══╝██║░░██║██╔════╝  ██╔══██╗██╔════╝██╔══██╗██║░░░░░  ░██║░░██╗░░██║██║██╔════╝██║
 ░░░██║░░░███████║█████╗░░  ██████╔╝█████╗░░███████║██║░░░░░  ░╚██╗████╗██╔╝██║█████╗░░██║
 ░░░██║░░░██╔══██║██╔══╝░░  ██╔══██╗██╔══╝░░██╔══██║██║░░░░░  ░░████╔═████║░██║██╔══╝░░██║
 ░░░██║░░░██║░░██║███████╗  ██║░░██║███████╗██║░░██║███████╗  ░░╚██╔╝░╚██╔╝░██║██║░░░░░██║
 =========================================================================================
 SetNext(ForDEVS)  <------------------------------------------------------------->  v1.0.0
 =========================================================================================
 
 ----------------""")

choose = input(" [1]=[COMEÇAR]\n [2]=[SAIR]\n ----------------\n ―>")



def TheRealWIFI():
    print("\n  Verificando...")
    import speedtest


    MyTest = speedtest.Speedtest()


    #<--DOWNLOAD-->#
    downloadSpeed = MyTest.download()
    #<--DOWNLOAD-->#


    #<--UPLOAD-->#
    uploadSpeed = MyTest.download()
    #<--UPLOAD-->#


    #<--PING-->#
    PING = MyTest.results.ping
    #<--PING-->#

    os.system('cls')

    print(f"""
 ●TheRealWIFI
 ---------------------------------
 ►Download: {downloadSpeed / 10**6:.2f}
 ►Upload: {uploadSpeed / 10**6:.2f}
 ►PING: {PING:.2f}
 ---------------------------------""")
    
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
print("\n ATENÇÃO!\n Abra o programa novamente, você não digitou 1 e nem 2.")
sleep(5)