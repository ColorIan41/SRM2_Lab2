import numpy as np
import matplotlib.pyplot as plot
from sympy.abc import x
import sympy as sp

x_arr = [-3, -1, 1, 3]
y_arr = [-0.18, 1.35, 1.78, 3.32]

x_arr1 = [-3, 0, 1, 3]
y_arr1 = [-0.18, 1.57, 1.78, 3.32]

plot.plot(x_arr, y_arr, marker='o', color='r', ls='', markersize=10)


def func(x):
    return 2 * np.arctan(np.sqrt(x ** 2 + 1) - x) + x


def grad(x, y, a, b):
    if a == 0: return y[b]
    return (grad(x, y, a - 1, b) - grad(x, y, a - 1, a - 1)) / (x[b] - x[a - 1])


def newton(x_array, y_array, x):
    yres = 0
    for p in range(len(x_array)):
        prodres = grad(x_array, y_array, p, p)
        for q in range(p):
            prodres *= (x - x_array[q])
        yres += prodres
    return yres

print("Поліном Ньютона:")

prange = np.linspace(x_arr[0], x_arr[-1], 200)
prange1 = np.linspace(x_arr1[0], x_arr1[-1], 200)

plot.plot(prange, func(prange), label='arcctg(x)+x')

print(sp.Poly(newton(x_arr, y_arr, x)))
plot.plot(prange, newton(x_arr, y_arr, prange), label='Newton polynomial, diapason 1')

print(sp.Poly(newton(x_arr1, y_arr1, x)))
plot.plot(prange1, newton(x_arr1, y_arr1, prange1), label='Newton polynomial, diapason 2')
plot.legend()
plot.show()

print("\nПохибка(Діапазон 1):")
print(np.abs(func(-0.5) - newton(x_arr, y_arr, -0.5)))
print("\nПохибка(Діапазон 2):")
print(np.abs(func(-0.5) - newton(x_arr1, y_arr1, -0.5)))
