import csv, time
import datetime
def what_software(title):
    dash_separated = title.split('-')
    if len(dash_separated) > 1:
        return dash_separated[-1]
    else:
        return dash_separated[0]
    
    
if __name__ == "__main__":
    with open('./window1.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['name', 'age'])
        
    Dict = {}
    with open('./window2.csv', 'r') as file:
        reader = csv.reader(file)
        table = list(reader)
    for i in range(1, len(table)-1):
        name = what_software(table[i][0]).strip().capitalize()
        next_time = datetime.datetime.strptime(table[i+1][1], "%Y-%m-%d %H:%M:%S")
        start_time = datetime.datetime.strptime(table[i][1], "%Y-%m-%d %H:%M:%S")
        if name != '' and name!= ' ':
            if name not in Dict:
                Dict[name] = next_time - start_time
            else:
                Dict[name] += next_time - start_time
        
    print('\033c', end='')
    for key in dict(sorted(Dict.items(), key=lambda item: item[1], reverse=True)):
        if Dict[key] > datetime.timedelta(seconds=1):
            print(key, Dict[key])
    