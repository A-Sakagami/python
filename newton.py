import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

# ニュートン法の関数
def f(z):
    return z**4 - 1

# ニュートン法の導関数
def df(z):
    return sym.Derivative(z)

# ニュートンダイアグラムの描画
x, y = np.meshgrid(np.linspace(-2, 2, 5000), np.linspace(-2, 2, 5000))
z = x + 1j*y
tol = 1e-6  # 収束条件
max_iter = 100  # 最大反復回数
colors = np.zeros_like(z, dtype=np.int32)

for i in range(max_iter):
    z -= f(z) / df(z)
    mask = (abs(f(z)) < tol) & (colors == 0)
    colors[mask] = i + 1

plt.imshow(colors, extent=[-2, 2, -2, 2], cmap='viridis')
plt.colorbar()
plt.title('Newton Fractal')
plt.xlabel('Re(z)')
plt.ylabel('Im(z)')
plt.show()
