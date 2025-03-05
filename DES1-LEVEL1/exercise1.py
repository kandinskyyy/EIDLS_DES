# определение состояния объекта 
velocity = float(input("введите скорость (м/с): "))
if velocity == 0:
    print ("объект в покое")
elif velocity > 0:
    print ("объект в движении")
else:
    print ("объект движется назад")