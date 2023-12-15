import datetime, os, time, csv
import pygetwindow as gw

def get_active_window():
    active_window = gw.getActiveWindow()
    return active_window.title if active_window else None

def format_time(time):
    return time.strftime("%Y-%m-%d %H:%M:%S")

if __name__ == "__main__":
    window_list = []
    if(os.path.exists('./windowTest.csv') == True):
        with open('./windowTest.csv', 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            table = list(reader)
        window_list = table[1:-1]
        
    script_start_time = format_time(datetime.datetime.now())
    window_list.append((get_active_window(), script_start_time, 'INF'))
    while True:
        current = get_active_window()
        currentTime = format_time(datetime.datetime.now())
        if current != window_list[-1][0]:
            print("Current window:", current, "Duration of last app:", currentTime)
            window_list[-1] = (window_list[-1][0], window_list[-1][1], currentTime)
            window_list.append((current, currentTime, 'INF'))
        time.sleep(1)
        with open('windowTest.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['window', 'start time', 'end time'])
            writer.writerows(window_list)
            