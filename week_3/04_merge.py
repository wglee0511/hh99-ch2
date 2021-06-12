array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]


def merge(array1, array2):
    new_arr = []
    a_index = 0
    b_index = 0

    while a_index < len(array1) and b_index < len(array2):
        if array1[a_index] < array2[b_index] :
            new_arr.append(array1[a_index])
            a_index += 1
        else :
            new_arr.append(array2[b_index])
            b_index += 1

    if a_index == len(array1) :
        while b_index < len(array2) :
            new_arr.append(array2[b_index])
            b_index += 1
    if b_index == len(array2) :
        while a_index < len(array1) :
            new_arr.append(array1[a_index])
            a_index += 1       

    return new_arr


print(merge(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!