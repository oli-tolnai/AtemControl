import PyATEMMax
from pynput.keyboard import Key, Listener, KeyCode
from pynput import keyboard
import win32gui, win32process, os


cmd = 'mode 16,6'
os.system(cmd)


atemMini = PyATEMMax.ATEMMax()
atem4K = PyATEMMax.ATEMMax()

atemMini.connect("192.168.1.223")
atemMini.waitForConnection(infinite=False)

atem4K.connect("192.168.1.221")
atem4K.waitForConnection(infinite=False)

pressed = False

def on_press(key):
    global pressed
    global PVW
    global PGM
    focus_window_pid = win32process.GetWindowThreadProcessId(win32gui.GetForegroundWindow())[1]
    current_process_pid = os.getppid()

    if focus_window_pid == current_process_pid:
        if key == keyboard.Key.esc:
            atem4K.disconnect()
            atemMini.disconnect()
            return False  # stop listener
        try:
            k = key.char  # single-char keys
        except:
            k = key.name  # other keys
        if k in ['1', '2', '3', '4'] and k != PVW and k != PGM:  # keys of interest
            # self.keys.append(k)  # store it in global-like variable
            PVW = k
            os.system('cls')
            print(f"PVW: {PVW}")
            print(f"PGM: {PGM}")
            kInt = int(k)
            # print(type(kInt))
            atem4K.setPreviewInputVideoSource(1, kInt) # set PVW on Atem4K M/E 2
        if k in ['5', '6', '7', '8'] and k != PVW and k != PGM:
            PVW = k # k
            os.system('cls')
            kInt = int(k)-4
            print(f"PVW: {PVW}")
            print(f"PGM: {PGM}")
            atemMini.setProgramInputVideoSource(0, kInt) # set PGM on AtemMini M/E 1
            atem4K.setPreviewInputVideoSource(1, 5) # set PVW on Atem4K M/E 2
        while key == keyboard.Key.space and pressed == False and PVW != "-1" and PVW != "0":
            temp = PGM
            PGM = PVW
            PVW = temp
            os.system('cls')
            print(f"PVW: {PVW}")
            print(f"PGM: {PGM}")
            print("CUT")
            atem4K.execCutME(1) #Cut on Atem4K M/E 2
            pressed = True
        while key == keyboard.Key.enter and pressed == False and PVW != "0" and PVW != "-1":
            atem4K.execAutoME(1)
            temp = PGM
            PGM = PVW
            PVW = temp
            os.system('cls')
            print(f"PVW: {PVW}")
            print(f"PGM: {PGM}")
            print("FADE")
            pressed = True
PVW = "-1"
PGM = "0"

def on_release(key):  # The function that's called when a key is released
    global pressed
    pressed = False


if not atem4K.connected and not atemMini.connected:
    os.system('cls')
    with Listener(on_press=on_press, on_release=on_release) as listener: listener.join()
else:
    os.system('cls')
    print("CONNECTION\nERROR")
    atem4K.disconnect()
    atemMini.disconnect()

# listener = keyboard.Listener(on_press=on_press)
# listener.start()  # start to listen on a separate thread
# listener.join()  # remove if main thread is polling self.keys


# Collect events until released
# with Listener(on_press=on_press) as listener:listener.join()

# 1 2 3 4 5 6 7 8 Keys
# 1 2 3 4 5 5 5 5 Atem4K PVW
# x x x x 1 2 3 4 AtemMini PGM

