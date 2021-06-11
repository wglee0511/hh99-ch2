input = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    tem_num = 0
    for each in array :
        if each > tem_num :
            tem_num = each
    return tem_num


result = find_max_num(input)
print(result)