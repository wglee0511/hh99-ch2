input = [4, 6, 2, 9, 1]
'''
4 6 2 9 1 # 1
1 | 6 2 9 4 # 2 
1 2 | 6 9 4 # 4
1 2 4 6 9
'''
def selection_sort(array):
    array_len = len(array)

    for each in range(array_len - 1) :
        min_index = each
        for each_se in range(each, array_len) : 
            if array[each_se] < array[min_index] :
                min_index = each_se
        array[each], array[min_index] = array[min_index] ,array[each]

    return


selection_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!