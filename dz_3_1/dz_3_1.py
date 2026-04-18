first_number = float(input("Введите первое число: "))
second_number = float(input("Введите второе число: "))
operation = input("Введите Операцию например (+, -, *, /): ")
if operation == "+":
    result = first_number + second_number
elif operation == "-":
    result = first_number - second_number
elif operation == "*":
    result = first_number * second_number
elif operation == "/":
    if second_number == 0:
        result = "на 0 делить нельзя"
    else:
        result = first_number / second_number
else:
    result = "Неверная операция"
#2 задание