# Теория
# Математика: Решение уравнений вида ax+b=0
# Физика: Равномерное прямолинейное движение: x(t) = x0 + v * t
# Программирование: Функции с параметрами.

## Моделирование положения объекта
try:
    v  = float(input("Введите скорость (м\с): "))                                                    #скорость м/с
    t  = float(input("Введите время (сек): "))                                                       # время сек
    x0 = float(input("Введите начальную позицию объекта (расстояние от точки отсчёта в метрах): "))  # начальная позиция

    def position (x0, velocity, time):
        return x0 + velocity * time

    result = position(x0, v, t)
    print(f"позиция через {t:2f} сек: {result:2f} м ")
except ValueError:
    print("ошибка введите чиловые значения!")

