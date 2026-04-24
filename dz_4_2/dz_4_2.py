list_of_numbers = input("Введите числа:  ").split(', ')
sum_of_numbers = 0

for index, num in enumerate(list_of_numbers):
 if index % 2 == 0:
  sum_of_numbers += int(num)

result = sum_of_numbers * int(list_of_numbers[-1])
#task 3 completed