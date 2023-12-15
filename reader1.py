import csv, time
import datetime
def what_software(title):
    dash_separated = title.split('-')
    if len(dash_separated) > 1:
        return dash_separated[-1]
    else:
        return dash_separated[0]
    
    

def format_time(time):
    return time.strftime("%Y-%m-%d %H:%M:%S")

while True:
# if __name__ == '__main__':     
    Dict = {}
    with open('./windowTest.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        table = list(reader)
    for i in range(1, len(table)-1):
        name = what_software(table[i][0]).strip().capitalize()
        if(table[i][2] == 'INF'):
            if(datetime.datetime.strptime(table[i][1], "%Y-%m-%d %H:%M:%S") != datetime.now().date()):
                continue
            else:
                end_time = datetime.datetime.now()
        else:
            end_time = datetime.datetime.strptime(table[i][2], "%Y-%m-%d %H:%M:%S")
        start_time = datetime.datetime.strptime(table[i][1], "%Y-%m-%d %H:%M:%S")
        if name != '' and name!= ' ':
            if name not in Dict:
                Dict[name] = end_time - start_time
            else:
                Dict[name] += end_time - start_time
        
    print('\033c', end='')
    for key in dict(sorted(Dict.items(), key=lambda item: item[1], reverse=True)):
        if Dict[key] > datetime.timedelta(seconds=0):
            print(key, Dict[key])
            
    total_time = datetime.timedelta(seconds=0);
    for key in Dict.keys():
        total_time += Dict[key]
    print("Total Time: ", total_time)
    time.sleep(4)