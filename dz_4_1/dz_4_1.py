
main_elements = [1, 21, 0, 33, 68, 0, 44, 0, 11, 52, 67]
result_with_zero_at_the_end = list()
count_of_zero = 0

for element in main_elements:
    if element != 0:
        result_with_zero_at_the_end.append(element)
    else:
        count_of_zero += 1

result_with_zero_at_the_end = result_with_zero_at_the_end + [0] * count_of_zero
# task 1 completed