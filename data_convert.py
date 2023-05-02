import json
import os
import pandas as pd
dir_name = os.path.dirname(__file__)
file=dir_name+'/OpcUA_PANE_BZ___2021_12_21__11_39_28.json'
data = [json.loads(line) for line in open(file,'r')]
df=pd.json_normalize(data)

df.to_csv(dir_name+'/out.csv', index=False)  

