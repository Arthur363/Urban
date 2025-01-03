print("Добро пожаловать в программу калкулятор!")

number1 = input("Введите первое число: ")
number1 = float(number1)

operation = input("Выберите арифметическую операцию (+, -, *, /): ")

number2 = input("Введите второе число: ")
number2 = float(number2)

if operation == '+':
    result = number1 + number2
elif operation == '-':
    result = number1 - number2
elif operation == '*':
    result = number1 * number2
elif operation == '/':
    if number2 != 0:
        result = number1 / number2
    else:
        result = "Деление на ноль!"
else:
    result = "Недопустимая операция!"

print("Результат:", result)

print("До свидания!")