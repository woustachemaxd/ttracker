import datetime
import time
import pygetwindow as gw
import pandas as pd

def get_active_window():
    active_window = gw.getActiveWindow()
    return active_window.title if active_window else None

def format_time(time):
    return time.strftime("%Y-%m-%d %H:%M:%S")

if __name__ == "__main__":
    script_start_time = format_time(datetime.datetime.now())
    window_list = []
    window_list.append((get_active_window(), script_start_time, 'INF'))
    
    while True:
        current = get_active_window()
        currentTime = format_time(datetime.datetime.now())
        
        if current != window_list[-1][0]:
            print("Current window:", current, "Duration of last app:", currentTime)
            window_list[-1] = (window_list[-1][0], window_list[-1][1], currentTime)
            window_list.append((current, currentTime, 'INF'))
        
        time.sleep(1)
        
        # Convert the window_list to a DataFrame
        df = pd.DataFrame(window_list, columns=['window', 'start time', 'end time'])
        
        # Write the DataFrame to a Feather file
        df.to_feather('windowTest.feather')
