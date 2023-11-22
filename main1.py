import numpy as np
import math

# Дано
H = 2
S = 10
v0 = 15
g = 10

angles_degrees = [35.5, 65.8]
angles_radians = [math.radians(angle) for angle in angles_degrees]
# Перевод в радианы, т.к. многие математические функции в Python (например, math.sin, math.cos, math.tan) используют радианы в качестве аргументов


# Функция для вычисления времени полёта
def time_fly(angle, speed):
    return S / (speed * math.cos(angle))

# Функция для вычисления длины траектории
def traector_length(angle, speed):
    t = time_fly(angle, speed)
    return S * math.tan(angle) - ((g * S**2) / (2 * speed**2 * math.cos(angle)**2))

# Нахождение длины траектории для каждого угла
for i, angle_rad in enumerate(angles_radians):
    length = traector_length(angle_rad, v0)
    print(f"Длина траектории движения шарика равна {length:.3f} метров, для угла вылета {angles_degrees[i]} градусов")

