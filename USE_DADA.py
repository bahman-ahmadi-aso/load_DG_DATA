
"""
@author: Bahman Ahmadi
"""
#______________________________________________________________________________
import sys,os,time,numpy as np,pandas as pd,matplotlib.pyplot as plt
from datetime import datetime
from SOL import SOL 
Param=SOL()

DU='oneday' # 'oneyear' or 'oneday'  #showing the duration of the simulation
SameLoadCurve="yes"    #if yes, the same load curve behavior is used for all nodes, other wise, the load curve behaviod is different for each node based on the curves in the csv file
Base_load_data="yes"   #yes: the maximum load is always 1, no: the load data for each day can be any number from 0 to 1 and not necessary can be 1 for max load

#load system data
active_power_time_series = pd.read_csv("data/time_series/active_power_scaled_"+DU+".csv",index_col=0,parse_dates=True).values
reactive_power_time_series = pd.read_csv("data/time_series/reactive_power_scaled_"+DU+".csv",index_col=0,parse_dates=True).values
LoadData = pd.read_csv("data/grid_data/Nodes_33.csv",index_col=0,parse_dates=True)
maxP=LoadData["PD"].values
maxQ=LoadData["QD"].values

if SameLoadCurve=="yes":
	ap=np.array([[active_power_time_series[t][0] for n in range(len(maxP))] for t in range(len(active_power_time_series))])
	aq=np.array([[reactive_power_time_series[t][0] for n in range(len(maxP))] for t in range(len(active_power_time_series))])
	P_profiles1=maxP*ap
	Q_profiles1=maxQ*aq
	if Base_load_data=="yes":
		scale=np.array([active_power_time_series[t][0] for t in range(len(active_power_time_series))])
		scale=scale/np.max(scale)
		ap=np.array([[scale[t] for n in range(len(maxP))] for t in range(len(active_power_time_series))])
		aq=np.array([[scale[t] for n in range(len(maxP))] for t in range(len(active_power_time_series))])
		P_profiles1=maxP*ap
		Q_profiles1=maxQ*aq
	Param.P_profiles=P_profiles1[:,:-1]
	Param.Q_profiles=Q_profiles1[:,:-1]
else:
	P_profiles1=maxP*active_power_time_series
	Q_profiles1=maxQ*reactive_power_time_series
	Param.P_profiles=P_profiles1[:,:-1]
	Param.Q_profiles=Q_profiles1[:,:-1]


#PV--WT
Param.PV = [val for sublist in pd.read_csv("data/time_series/photovoltaic_"+DU+".csv",index_col=0,parse_dates=True).values.tolist() for val in sublist for i in range(2)]
Param.WT = [val for sublist in pd.read_csv("data/time_series/windturbine_"+DU+".csv",index_col=0,parse_dates=True).values.tolist() for val in sublist for i in range(2)]




a=1