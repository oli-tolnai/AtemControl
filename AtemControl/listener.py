from pynput.keyboard import Listener
import  pynput


pressed = False
def on_press(key):  # The function that's called when a key is pressed
    #global pressed
    print("Key pressed: {0}".format(key))
    #if key == pynput.keyboard.Key.space:# and pressed == False:
     #   print("Key pressed: {0}".format(key))
        # pressed = True

def on_release(key):  # The function that's called when a key is released
    #global pressed
    #print("Key released: {0}".format(key))
    if key == pynput.keyboard.Key.space:# and pressed == False:
        print("Key released: {0}".format(key))
    #pressed = False

with Listener(on_press=on_press, on_release=on_release) as listener:  # Create an instance of Listener
    listener.join()



##EZ A JÓ##
# pressed = False
# def on_press(key):  # The function that's called when a key is pressed
#     global pressed
#     if key == pynput.keyboard.Key.space:# and pressed == False:
#         print("Key pressed: {0}".format(key))
#         pressed = True
#
# def on_release(key):  # The function that's called when a key is released
#     global pressed
#     print("Key released: {0}".format(key))
#     pressed = False
#
# with Listener(on_press=on_press, on_release=on_release) as listener:  # Create an instance of Listener
#     listener.join()