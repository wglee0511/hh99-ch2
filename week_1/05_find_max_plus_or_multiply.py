input = [0, 3, 5, 6, 1, 2, 4]


def find_max_plus_or_multiply(array):
    temp_result = 0
    for each in array :
        if each <= 1 or temp_result <= 1:
            temp_result = temp_result + each
        else :
            temp_result = temp_result * each
    return temp_result

result = find_max_plus_or_multiply(input)
print(result)