# Напишите код, который запрашивает число и сообщает является ли оно простым или составным. Используйте правило для
# проверки: “Число является простым, если делится нацело только на единицу и на себя”. Сделайте ограничение на ввод
# отрицательных чисел и чисел больше 100 тысяч.

MIN_NUM = 0
MAX_NUM = 100000
divider = 2
count = 0
number = int(input('Введите число: '))
if number < MIN_NUM or number > MAX_NUM:
    print('Число не соотвествует заданному диапазону!')
elif number == 0 or number == 1:
    print('Числа 0 и 1 не являются ни простыми, ни составными числами')
else:
    for i in range(divider, number):
        if number % i == 0:
            count += 1
            break
    if count == 1:
        print("число составное ")
    else:
        print("число простое")

MIN_NUM = 0
MAX_NUM = 100000
divider = 2
number = int(input('Введите число: '))
if number < MIN_NUM or number > MAX_NUM:
    print('Число не соотвествует заданному диапазону!')
elif number == 0 or number == 1:
    print('Числа 0 и 1 не являются ни простыми, ни составными числами')
else:
    for i in range(divider, number):
        if number % i == 0:
            print("число составное ")
            break1
    else:
        print("число простое")