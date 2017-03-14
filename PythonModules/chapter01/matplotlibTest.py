#-*-coding:utf-8-*-
import matplotlib

import numpy as np

import matplotlib.pyplot as plt


#-*-coding:utf-8-*-

x = np.linspace(0,10,1000)

y = np.sin(x)

z= np.cos(x ** 2)

#创建一个绘图对象，如果不创建就会自动创建
# plt.figure(figsize=(8,4))

# #传入x和y
# plt.plot(x,y,label="$sin(x)$",color="red",linewidth=2)

# plt.plot(x,z,"b--",label="$cos(x^2)$")

# plt.xlabel("Time(s)")

# plt.title("PyPlot First Example")

# plt.ylim(-1.2,1.2)

# plt.legend()

# plt.show()

arr1 = np.linspace(-10,10,1000)

arr2 = arr1 ** 3

fig = plt.figure()

plt.plot(arr1,arr2,label="$张三李四$")
plt.show()