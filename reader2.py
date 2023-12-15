import time
import datetime
import pandas as pd

def what_software(title):
    dash_separated = title.split('-')
    if len(dash_separated) > 1:
        return dash_separated[-1]
    else:
        return dash_separated[0]

if __name__ == "__main__":
    
    
    df = pd.read_feather('windowTest.feather')
    Dict = {}
    
    for i in range(1, len(df)-1):
        name = what_software(df['window'][i]).strip().capitalize()
        
        if df['end time'][i] == 'INF':
            end_time = datetime.datetime.now()
        else:
            end_time = datetime.datetime.strptime(df['end time'][i], "%Y-%m-%d %H:%M:%S")
        
        start_time = datetime.datetime.strptime(df['start time'][i], "%Y-%m-%d %H:%M:%S")
        
        if name != '' and name != ' ':
            if name not in Dict:
                Dict[name] = end_time - start_time
            else:
                Dict[name] += end_time - start_time

    print('\033c', end='')
    
    for key in dict(sorted(Dict.items(), key=lambda item: item[1], reverse=True)):
        if Dict[key] > datetime.timedelta(seconds=0.5):
            print(key, Dict[key])

