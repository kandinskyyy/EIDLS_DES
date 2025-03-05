# Расчёт давления на поверхность

# Математика
# Площадь прямоугольника: s = a*b
# Площадь круга: s = pi * r^2
# Физика
# Давление: P = F/S

import math

force = float(input("Введите силу (Н): "))
radius = float(input("Ведите радиус круга(м): "))
area = math.pi * radius**2
pressure = force / area 
print(f"Давление: {pressure:.2f} Па")