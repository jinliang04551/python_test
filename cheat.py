#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from scipy.stats import pearsonr
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
import os


# 处理异常（0）的数据，丢掉含 0 的行
def transformZero(x):
    try:
        tmp = float(x)
        if tmp > 0:
            return tmp
        else:
            return np.nan
    except:
        return np.nan


# 处理函数，输入文件名，是否画图、是否需要绝对差中位数、是否输出皮尔森
# 返回  皮尔森系数 和 绝对差中位数
def processFile(file_name, show_plot = True, show_pearson = True, show_medium_diff = True):

    HR_keys = ["HR","HR.1"]

    init_df = pd.read_csv(file_name, header=1, names=None)

    df = init_df[HR_keys].dropna()

    for key in HR_keys:
        df[key] = df[key].map(transformZero)

    df = df.dropna()

    # x = []

    # for i in range(0,500):
    #     x.append(random.randint(80, 150))      # 80 - 150随机

    # y = []

    # for x_item in x:
    #     y.append(x_item + random.randint(-35, 35))    # 增加 -10 到 10 的随机值
    #     # y.append(random.randint(80, 150))

    # print("x:",x,"\n")


    # print("y:",y,"\n")

    if show_plot:
        plt.figure()
        plt.xlabel('Time')
        plt.ylabel('HR')
        plt.plot(df["HR"], label='HR1')
        plt.plot(df["HR.1"], label='HR2')


        plt.legend()
        plt.show()



    pearson = pearsonr(df["HR"], df["HR.1"])
    medium_diff = np.median(np.abs(df["HR"] - df["HR.1"]))
    
    print("Result of experiment ",file_name,":\n")

    print("HR1 & HR2:\n")

    if show_pearson:
        print("皮尔森系数:",pearson[0])

    if show_medium_diff: 
        print("绝对差中位数:",medium_diff)

    
    print("\n--------------------------\n")

    # print("HR2 & HR3:")
    # print("pearson:",pearsonr(df["HR2"], df["HR3"]),"\n")

    # print("HR1 & HR3:")
    # print("pearson:",pearsonr(df["HR1"], df["HR2"]),"\n")
    return pearson[0], medium_diff


inputFile = ""

if len(sys.argv) > 1:
    inputFile = sys.argv[1]
else:
    print("请输入一个asv文件")
    exit()

if os.path.exists(inputFile) == False:
    print("文件不存在，请检查")
    exit()

a,b = processFile(inputFile, show_plot = False, show_pearson = True, show_medium_diff = True)

if a > 0.90 and b < 10:
    print("结论：极有可能为作弊情况")
else:
    print("结论：非作弊情况")
