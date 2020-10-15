import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-10,10)  
plt.ylim(0,5)                          
plt.subplot(221)
plt.title(u'exp(-0.4*t)')
ft = np.exp(-0.4*t)          
plt.plot(t,ft) 
plt.subplot(222)
plt.title(u'exp(0.4*t)')
ft1 = np.exp(0.4*t)
plt.plot(t,ft1)
plt.subplot(212)
plt.title(u'exp(0*t)')
ft2 = np.exp(0*t)
plt.plot(t,ft2)
plt.show()