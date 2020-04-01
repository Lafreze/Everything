# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import os
path="/給料/"
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
            if '時間外勤務手当' in str(file_csv[lo].loc[li]) :
                zangyou.append(int(str(file_csv[lo+1].loc[li]).replace(',','')))
            elif '支給内容計' in str(file_csv[lo].loc[li]) :
                salary.append(int(str(file_csv[lo+1].loc[li]).replace(',','')))
            elif '銀行振込額' in str(file_csv[lo].loc[li]) :
                get_money.append(int(str(file_csv[lo+1].loc[li]).replace(',','')))
            elif '引去内容計' in str(file_csv[lo].loc[li]) :
                out_money.append(int(str(file_csv[lo+1].loc[li]).replace(',','')))
            elif '給与明細' in str(file_csv[lo].loc[li]) :
                date_list.append(file_csv[lo].loc[li+1].replace('\"','').replace('=20',''))
            elif '所得税' in str(file_csv[lo].loc[li]) :
                tax_list.append(int(str(file_csv[lo+1].loc[li]).replace(',','')))
    if len(zangyou)<len(date_list):
        zangyou.append(0)


matplotlib.rcParams['font.family']='SimSun'
plt.plot(date_list, salary,label="支給内容計",marker="o")
plt.plot(date_list, get_money,label="銀行振込額",marker="o")
plt.plot(date_list, out_money,label="引去内容計",marker="o")
plt.plot(date_list, tax_list,label="所得税",marker=".")
plt.plot(date_list, zangyou,label="時間外勤務手当",marker=".")
for a,b in zip(date_list,salary):
    plt.annotate('%s'%b,xy=(a,b),xytext=(-20,10),
                 textcoords='offset points')
for a,b in zip(date_list,get_money):
    plt.annotate('%s'%b,xy=(a,b),xytext=(-20,10),
                 textcoords='offset points')
for a,b in zip(date_list,zangyou):
    plt.annotate('%s'%b,xy=(a,b),xytext=(-20,10),
                 textcoords='offset points')
plt.legend()
plt.xlabel('月',fontproperties='SimSun',fontsize=9)  
plt.ylabel('円',fontproperties='SimSun',fontsize=9)
plt.show()
