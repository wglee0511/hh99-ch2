input = [4, 6, 2, 9, 1]

'''
4  # 4
4 6  # 4
4 6 2 # 2
2 4 6 9 # 2
1 2 4 6 9 # 1

0 1 2 3 4
'''


def insertion_sort(array):
    array_len = len(array)
    for each in range(1,array_len):
        for each_se in range(each, 0, -1):
            if array[each_se - 1] > array[each_se] :
                array[each_se - 1], array[each_se] = array[each_se], array[each_se - 1]

    return


insertion_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!