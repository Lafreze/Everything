# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import os
import numpy as np
from matplotlib.ticker import MaxNLocator
import matplotlib.ticker as ticker
path="C:/../給料/"
#path = args.path
files= os.listdir(path)
fi_list = list(files)
salary = list()
get_money = list()
salary = list()
tax_list = list()
out_money = list()
zangyou = list()
date_list = list()
for file in fi_list:
    if file.split('.')[-1] not in ['csv']:
        continue
    file_csv = pd.read_csv(path+file, header=None, engine='python')

    loc_num = 6
    line_num = len(file_csv[1])
    for li in range(line_num-1):
        for lo in range(loc_num-1):
            #print(file_csv[lo].loc[li])
            if '時間外勤務手当' in str(file_csv[lo].loc[li]) :
                zangyou.append(round(int(str(file_csv[lo+1].loc[li]).replace(',',''))/1000))
            elif '支給内容計' in str(file_csv[lo].loc[li]) :
                salary.append(round(int(str(file_csv[lo+1].loc[li]).replace(',',''))/1000))
            elif '銀行振込額' in str(file_csv[lo].loc[li]) :
                get_money.append(round(int(str(file_csv[lo+1].loc[li]).replace(',',''))/1000))
            #elif '引去内容計' in str(file_csv[lo].loc[li]) :
                #out_money.append(int(str(file_csv[lo+1].loc[li]).replace(',',''))//10000)
            elif '給与明細' in str(file_csv[lo].loc[li]) :
                date_list.append(file_csv[lo].loc[li+1].replace('\"','').replace('=20',''))
            #elif '所得税' in str(file_csv[lo].loc[li]) :
                #tax_list.append(int(str(file_csv[lo+1].loc[li]).replace(',',''))//10000)
    if len(zangyou)<len(date_list):
        zangyou.append(0)


matplotlib.rcParams['font.family']='SimSun'
fig, ax1 = plt.subplots()
ax1.plot(date_list, salary,color='b',label="給料",marker="o")
ax1.plot(date_list, get_money,color='lightblue',label="手取り",marker="o")
#ax1.plot(date_list, out_money,label="引去内容計",marker="o")
#ax1.plot(date_list, tax_list,label="所得税",marker=".")
ax1.plot(date_list, zangyou,label="残業手当",marker="o")
ax2 = ax1.twinx()
sum_salary = np.cumsum(salary)
sum_get_money = np.cumsum(get_money)
ax2.plot(date_list,sum_salary,color='pink',label="給料総額",marker="x")
ax2.plot(date_list,sum_get_money,color='magenta',label="手取り総額",marker="x")

for a,b in zip(date_list,salary):
    ax1.annotate('%s'%b,xy=(a,b),xytext=(0,10),textcoords='offset points')
for a,b in zip(date_list,get_money):
    ax1.annotate('%s'%b,xy=(a,b),xytext=(0,10),textcoords='offset points')
for a,b in zip(date_list,zangyou):
    ax1.annotate('%s'%b,xy=(a,b),xytext=(0,10),textcoords='offset points')
for a,b in zip(date_list,sum_salary):
    ax2.annotate('%s'%b,xy=(a,b),xytext=(0,10),textcoords='offset points')
for a,b in zip(date_list,sum_get_money):
    ax2.annotate('%s'%b,xy=(a,b),xytext=(0,-10),textcoords='offset points')
handler1, label1 = ax1.get_legend_handles_labels()
handler2, label2 = ax2.get_legend_handles_labels()
ax1.legend(handler1 + handler2, label1 + label2, loc=2, borderaxespad=0.)

pageview_max = max(salary)
register_max = max(sum_salary)

ax1.set_ylim([0, 1.1*pageview_max])
ax2.set_ylim([0, 1.1*register_max])
plt.xlabel('月',fontproperties='SimSun',fontsize=9)
plt.ylabel('円(千)',fontproperties='SimSun',fontsize=9)
plt.show()
