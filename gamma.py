import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma

x = np.linspace(0, 5, 100)
y = gamma(x)

plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("Gamma(x)")
plt.title("Gamma Function")
plt.grid()
plt.show()
