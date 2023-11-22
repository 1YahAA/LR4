import numpy as np

a = 2
b = 3
num_points = 1000 # кол-во точек на эллипсе (для дискретизации)

# Функция для вычисления x и y на эллипсе для заданного угла alpha
def f(alpha):
    x = a * np.cos(alpha)
    y = b * np.sin(alpha)
    return x, y

# Вычисление координат точек на эллипсе для различных углов theta
alpha_values = np.linspace(0, 2 * np.pi, num_points)
ellipse_points = np.array([f(alpha) for alpha in alpha_values])

# Вычисление длины отрезков между точками
perimeter = np.sum(np.sqrt(np.sum(np.diff(ellipse_points, axis=0)**2, axis=1)))

print(f"Периметр эллипса: {perimeter:.10f}")