def calc_sum_of_numbers(elem):
    if elem == []:
        return 0
    else:
        sum = calc_sum_of_numbers(elem[1:])

        sum = sum + elem[0]
        return sum


result = calc_sum_of_numbers([23, 3, 5, 10, 13, 26])
print(result)