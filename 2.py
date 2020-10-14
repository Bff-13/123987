import numpy as np
import matplotlib.pyplot as plt
from pylab import *
x1 = np.arange(-10.0, 3.0, 0.01)
x2 = np.arange(-10.0, 10.0, 0.01)

y1 = np.exp(x1)
plt.subplot(2,3,1)
plt.plot(x1, y1)
plt.xlabel('t')
plt.ylabel('x(t)')
y2= np.cos(x2)
# plt.figure(3)
plt.subplot(2,3,2)
plt.plot(x2, y2)
y3= np.exp(-0.1*x2)*np.cos(x2)
plt.subplot(2,3,3)
plt.plot(x2, y3)
plt.xlabel('t')
plt.ylabel('x(t)')
y4= np.sin(x2)/x2
plt.plot(x2, y4)
# plt.subplot(2,3,4)
plt.xlabel('t')
plt.ylabel('x(t)')
def step_function1(x=''):
    if x >0:
        return 1
    else:
        return 0

def step_function2(x):

    y = x > 0  
    return y.astype(np.int)   

m = 1
print(step_function1(m))

x = np.arange(-5.0,5.0,0.1)  
y = step_function2(x)
plt.ylim(-0.1, 1.1)
plt.subplot(2,3,5)
plt.plot(x, y)
plt.xlabel('t')
plt.ylabel('x(t)')
plt.show() 