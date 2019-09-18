#!/usr/bin/python2.7
#*-----encoding=utf8-----*


# import matplotlib as mpl 
# mpl.use('TkAgg')
import numpy as np
import matplotlib.pyplot as plt 

# ====================================
# 柱状图
# ====================================
# x = np.array([1,2,3,4,5,6,7,8])
# y = np.array([3,5,7,6,2,6,10,15])
# plt.plot(x,y,'r')
# plt.plot(x,y,'g',lw=10)

# #折线 饼状 柱状
# x = np.array([1,2,3,4,5,6,7,8])
# y = np.array([13,25,17,36,21,16,10,15])
# plt.bar(x,y,0.2,alpha=1,color='b')
# plt.show()


# ====================================
# 柱状图2
# ====================================
# for i in range(0,15):
#     dateOne = np.zeros([2])
#     dateOne[0] = i
#     dateOne[1] = i
#     y = np.zeros([2])
#     y[0] = 10
#     y[1] = 20
#     plt.plot(dateOne,y,'r',lw=8)
# plt.show()


# ====================================
# 绘制 y =2x+1 函数的图像
# ====================================
# x = np.linspace(-1,1,66)
# y = 2*x + 1
# plt.plot(x,y)
# plt.show()


# ====================================
# 绘制x^2 函数的图像
# ====================================
# x = np.linspace(-1,1,66)
# y = x**2
# plt.plot(x,y)
# plt.show()


# ====================================
# figure的使用
# ====================================
# x = np.linspace(-1,1,50)
# # figure 1
# y1 = 2 *x + 1
# plt.figure()
# plt.plot(x,y1)

# # figure 2
# y2 = x**2
# plt.figure()
# plt.plot(x,y2)

# # figure 3，指定figure的编号并指定figure的大小, 指定线的颜色, 宽度和类型
# #一个坐标轴上画了两个图形
# y2 = x **2
# plt.figure(num=5,figsize=(4,4))
# plt.plot(x,y1)
# plt.plot(x,y2,color= 'red',linewidth=1.0, linestyle ='--')
# plt.show()


# ====================================
# 设置坐标轴
# ====================================
# x = np.linspace(-1,1,50)
# y1 = 2 *x +1
# y2 =x**2
# plt.figure()
# plt.plot(x,y1)
# plt.plot(x,y2,color = 'red', linewidth= 1.0,linestyle ='--')

# # 设置坐标轴的取值范围
# plt.xlim((-1,1))
# plt.ylim((0,3))

# # 设置坐标轴的lable


# ====================================
# 动画
# ====================================
from matplotlib import animation

# 定义figure
fig, ax = plt.subplots()

# 定义数据
x = np.arange(0,2 * np.pi, 0.01)
line, = ax.plot(x,np.sin(x))


# 定义动画的更新
def update(i):
    line.set_ydata(np.sin(x + i/10))
    return line,

def init():
    line.set_ydata(np.sin(x))
    return line,

# 创建动画
ani = animation.FuncAnimation(fig = fig, func =update,init_func= init,interval = 10,blit =False, frames=200)
plt.show()

# 动画保存
ani.save('sin.html',writer='imageagick',fps=30,dpi=100)


# //正确显示中文
# git config --global core.quotepath false