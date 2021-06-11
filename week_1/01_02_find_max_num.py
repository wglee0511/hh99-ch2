input = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    for each in array:
        for compara_each in array:
            if each < compara_each :
                break
        else :
            return each


result = find_max_num(input)
print(result)