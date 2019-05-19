import numpy as np
import datetime

def random_list(n):
    ''' Returns a list of random normal variables'''
    return [np.round(k, 2) for k in list(np.random.normal(size=n).cumsum())]


def named_series(names):
    ''' Returns a list of dictionaries with "name" as string and "data" as a list of floats'''
    return [{"name": name, "data": random_list(60)} for name in names]


def daily_range(start=datetime.date.today(), days=60):
    ''' Create a range of n days. Default start is today'''
    drange = [start]
    
    [drange.append(drange[-1] + datetime.timedelta(hours=24)) 
        for _ in range(days) ]
        
    return [i.strftime("%d-%b") for i in drange]
