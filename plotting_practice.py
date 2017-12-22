import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 20)
y = np.sin(x)
plt.subplot(2, 1, 1)
plt.title('a few plots')
plt.plot(x, x, 'k-o', label = 'linear')
plt.legend()
plt.subplot(2, 1, 2)
plt.plot(x, y, 'b.-', label = 'sine')
plt.annotate('sin', xy=(3.2,0.2), xytext=(3.6, 0.4),
    arrowprops=dict(arrowstyle="->"))
#plt.legend()
plt.show()
