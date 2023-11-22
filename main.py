import numpy as np
from scipy.integrate import trapz

# Определяем функцию y = x^2
def f(x):
    return x**2

# Задаем интервал
a = 0
b = 10
n = 1000  # Количество точек для интегрирования

# Создаем массив значений x на интервале [0, 10]
x = np.linspace(a, b, n)

# Вычисляем значения функции на этом интервале
y = f(x)

# Вычисляем производную функции y = x^2
proizvodnaya = np.gradient(y, x)

# Вычисляем длину кривой методом трапеций
curve_length = trapz(np.sqrt(1 + proizvodnaya**2), x)

print(f"Длина кривой y = x**2 на интервале [0, 10]: {curve_length:.4f}")