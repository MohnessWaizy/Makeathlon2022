""" Detects Point Anomaly using Z score"""

import pandas as pd
import os
import scipy.stats as ss
import numpy as np
import matplotlib.pyplot as plt

def plot_anomaly(score_data, threshold,row_,col_):
    score_data = df['zscore']
    ranks = np.linspace(1, len(score_data), len(score_data))
    mask_outlier = []

    # scores that are greater than 1 are considered anomalies since we are interested to detect the dough with higher thickness
    mask_outlier = (score_data > threshold) 
    axs[col_].plot(ranks[~mask_outlier], score_data[~mask_outlier],'.', color='b',label='OK values')
    axs[col_].plot(ranks[mask_outlier], score_data[mask_outlier],'.', color='r', label='Anomalies')
    axs[col_].axhline(threshold,color='r',label='threshold', alpha=1)
    axs[col_].legend(loc = 'upper left')
    axs[col_].set_title('Point Anomaly \n Einlauf IST [mm]')

dir_name = os.path.dirname(__file__)
fig, axs = plt.subplots(1,2)
data=pd.read_csv(dir_name+"/data/OpcUA_PANE_BZ___2022_05_24__15_16_19.csv")
df = pd.DataFrame(data)
mean = data['distanceSensors[0].calcValueInMm'].mean()
std = data['distanceSensors[0].calcValueInMm'].std()
axs[0].plot(data["quadroSensorsAutoCommands[0].setpointInMm"],label='IST')
axs[0].plot(data["distanceSensors[0].calcValueInMm"],label='Soll')
axs[0].legend(loc = 'upper left')
zscore = ss.zscore(data['distanceSensors[0].calcValueInMm'])
df= df.assign(zscore=zscore)
plot_anomaly(df['zscore'], 1,0,1)
axs[0].set_title('Einlauf [mm]')
plt.show()  
