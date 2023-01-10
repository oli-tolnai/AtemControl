from os import system
import PyATEMMax
from time import sleep
import sys, time, threading

atemMini = PyATEMMax.ATEMMax()
atem4K = PyATEMMax.ATEMMax()


def connectToAtem():
    atemMini.connect("192.168.1.223")
    atemMini.waitForConnection(infinite=False)

    atem4K.connect("192.168.1.221")
    atem4K.waitForConnection(infinite=False)

def loadingAnimation(process) :
    while process.is_alive():
        chars = "/—\|"
        for char in chars:
            sys.stdout.write('\r'+'Connecting '+char)
            time.sleep(.1)
            sys.stdout.flush()

loading_process = threading.Thread(target=connectToAtem)
loading_process.start()

loadingAnimation(loading_process)
loading_process.join()


# if atem4K.connected and atemMini.connected:
#     system('cls')
#     print(f"MODE:\n")
#     print(f"PVW:")
#     print(f"PGM:")
# else:
#     system('cls')
#     print("Connection error")
#     atem4K.disconnect()
#     atemMini.disconnect()

# db = 0
# system('cls')
# while db < 100:
#     print("CONNECTING")
#     sleep(.2)
#     system('cls')
#     print("CONNECTING.")
#     sleep(.2)
#     system('cls')
#     print("CONNECTING..")
#     sleep(.2)
#     system('cls')
#     print("CONNECTING...")
#     sleep(.2)
#     system('cls')
#     db += 1

# animation = "|/-\\"
# idx = 0
# while True:
#     print(animation[idx % len(animation)], end="\r")
#     idx += 1
#     sleep(0.1)




# bar = [
#     " [=     ]",
#     " [ =    ]",
#     " [  =   ]",
#     " [   =  ]",
#     " [    = ]",
#     " [     =]",
#     " [    = ]",
#     " [   =  ]",
#     " [  =   ]",
#     " [ =    ]",
# ]
# i = 0
#
# while True:
#     print(bar[i % len(bar)], end="\r")
#     sleep(.2)
#     i += 1