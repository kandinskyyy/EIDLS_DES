distance = float(input("введите Расстояние (м): ")) 
time = float(input("введите время(сек): "))
speed = distance / time 
print (f"Скорость={speed} м/с")

speed = float(input("введите скорость (м/с): ")) 
distance = float(input("введите Расстояние (м): ")) 
time = distance / speed 
print ((f"время={time} сек"))

# Математика: сравнение чисел <>= 
# Физика: покой vs движение v!=0, ускорение: a = Δv/Δt
# Программирование: условные конструкции if elif else 

# определение состояния объекта 
velocity = float(input("введите скорость (м/с): "))
if velocity == 0:
    print ("объект в покое")
elif velocity > 0:
    print ("объект в движении")
else:
    print ("объект движется назад")

# math последовтательности (12345678)
# physic (равномерное движение s=v*t)
# prog цикл for

# расчет пройденного пути за каждую секунду
velocity = 2
total_time = 10
print("Секунда | расстояние")
for t in range(1, total_time +1 ):
    # distance = velocity * t
    print(f"{t}сек -> {total_time}м")

# расчет общей скорости v = s/t 
distance = int(input("введите Расстояние (м): ")) 
time = int(input("введите время(сек): "))
velocity=distance/time
print (f"скорость: {velocity} метров в секунду")

# Функция для расчёта силы тока

voltage = int(input("введите напряжение U: "))
resistance = int(input("введите сопротивление Ом: "))
def calculate_sila_toka(voltage, resistance):
    if resistance == 0:
        raise ValueError ("ошибка деление на 0, сопротивление не может быть 0")
    return voltage / resistance
print(f"Cила тока{calculate_sila_toka(voltage,resistance)} Ампер")