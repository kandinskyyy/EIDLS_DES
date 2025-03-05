# Функция для расчёта силы тока
voltage = int(input("введите напряжение U: "))
resistance = int(input("введите сопротивление Ом: "))
def calculate_sila_toka(voltage, resistance):
    if resistance == 0:
        raise ValueError ("ошибка деление на 0, сопротивление не может быть 0")
    return voltage / resistance
print(f"Cила тока{calculate_sila_toka(voltage,resistance)} Ампер")