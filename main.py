import time
import csv
import psutil
from datetime import datetime


def list_all_processes():
    all_processes = psutil.process_iter()
    process_info_list = []
    
    for process in all_processes:
        try:
            process_info = process.as_dict(attrs=['pid', 'name', 'username', 'status', 'create_time', 'cpu_times', 'memory_info', 'memory_percent'])
            process_info_list.append(process_info)
            create_time_datetime = datetime.fromtimestamp(process_info['create_time'])
            create_time_str = create_time_datetime.strftime("%Y-%m-%d %H:%M:%S")
            process_info['create_time'] = create_time_str
            process_info['cpu_times'] = str(datetime.now() - create_time_datetime)
        except (psutil.AccessDenied, psutil.ZombieProcess, psutil.NoSuchProcess):
            pass
    
    with open('process.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['pid', 'name', 'username', 'status', 'create_time', 'cpu_times', 'memory_info', 'memory_percent'])
        writer.writeheader()
        writer.writerows(process_info_list)
        
        
import time
import pygetwindow as gw

def get_active_window():
    active_window = gw.getActiveWindow()
    return active_window.title if active_window else None


if __name__ == "__main__":
    all_titles = gw.getAllTitles()
    focused_window = gw.getActiveWindow()
    with open('window.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(all_titles)
        writer.writerow(focused_window)
    
    # prev = None
    # script_start_time = datetime.now()
    # window_list = []
    # window_list.append((get_active_window(), script_start_time))
    # while True:
    #     current = get_active_window()
    #     if current != prev:
    #         currentTime = datetime.now()
    #         window_list.append((current, currentTime))
    #         duration = currentTime - window_list[-2][1]
    #         duration_str = str(duration)
    #         duration_str = duration_str.split(".")[0]
    #         print("Current window:", current, "Duration of last app:", duration_str)
    #         prev = current
    #     time.sleep(1)
    #     with open('window.csv', 'w', newline='') as f:
    #         writer = csv.writer(f)
    #         writer.writerows(window_list)
            
        
        
    
