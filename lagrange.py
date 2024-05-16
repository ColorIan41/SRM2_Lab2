import numpy as np
import matplotlib.pyplot as plot
from sympy.abc import x
import sympy as sp

#y=arcctg(x)+x
x_arr = [-3, -1, 1, 3]
y_arr = [-0.18, 1.35, 1.78, 3.32]

x_arr1 = [-3, 0, 1, 3]
y_arr1 = [-0.18, 1.57, 1.78, 3.32]

n = len(x_arr) - 1
prange = np.linspace(min(x_arr), max(x_arr), 500)
prange1 = np.linspace(min(x_arr1), max(x_arr1), 500)

plot.plot(x_arr, y_arr, marker='o', color='r', ls='', markersize=10)


def func(x):
    return 2 * np.arctan(np.sqrt(x ** 2 + 1) - x) + x


def lagrange(x, y):
    sum = 0
    for i in range(n + 1):
        prod = y[i]
        for j in range(n + 1):
            if i != j:
                prod = prod * (x - x_arr[j]) / (x_arr[i] - x_arr[j])
        sum = sum + prod
    return sum


print("Поліном Лагранжа:")

plot.plot(prange, func(prange), label='arcctg(x)+x')

print(sp.Poly(lagrange(x, y_arr)))
plot.plot(prange, lagrange(prange, y_arr), label='Lagrange polynomial, diapason 1')

print(sp.Poly(lagrange(x, y_arr1)))
plot.plot(prange1, lagrange(prange1, y_arr1), label='Lagrange polynomial, diapason 2')
plot.legend()
plot.show()

print("\nПохибка(Діапазон 1):")
print(np.abs(func(-0.5) - lagrange(-0.5, y_arr)))
print("\nПохибка(Діапазон 2):")
print(np.abs(func(-0.5) - lagrange(-0.5, y_arr1)))
