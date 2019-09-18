# -*- coding:utf-8-*-
#wan
#author liu

import tushare as ts 
import matplotlib.pyplot as plt
import datetime

tiker = '600028'
finace = ts.get_hist_data(tiker,'2017-12-30','2018-08-01')
