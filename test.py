import pandas as pd
import os
import scipy.stats as ss
import numpy as np
import pandas as pd

from datetime import datetime
dir_name = os.path.dirname(__file__)
data=pd.read_csv(dir_name+'/data/OpcUA_PANE_BZ___2021_12_21__10_33_00.csv')
inlet=data['distanceSensors[0].calcValueInMm']
flag=0
counter=0
date_format_str = '%H:%M:%S'
inlet_data=[]
p=0
for i in range (0,len(inlet)):
    if inlet[i]>165:
        flag=1
    if flag==1:
        if inlet[i]<150 and counter==0:
            first_time=data['time'].iloc[i]
            first_time=first_time[11:19]
            start = datetime.strptime(first_time, date_format_str)
            counter=1
        if counter==1 and inlet[i]<130:
            cur_time=data['time'].iloc[i]
            cur_time=cur_time[11:19]
            end =   datetime.strptime(cur_time, date_format_str)
            diff = end - start
            print('Difference between two datetimes in seconds:',first_time,)
            p=diff.total_seconds()
        inlet_data.append(inlet[i])
    if p>60:
        break
        
print(inlet_data)

