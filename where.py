import pygetwindow as gw
import time, json

def get_active_window():
    active_window = gw.getActiveWindowTitle()
    return active_window if active_window else "Home"

while True:
    with open("../electronTut/videoInfo/data.json", "w") as json_file:
        json.dump({"window": get_active_window()}, json_file)
    print(get_active_window())
    time.sleep(.4)