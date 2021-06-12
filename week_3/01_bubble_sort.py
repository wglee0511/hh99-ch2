input = [4, 6, 2, 9, 1]


def bubble_sort(array):
    for each in range(len(array) - 1) :
        for each_inner in range(len(array) - 1 - each) :
            if array[each_inner] > array[each_inner +1]:
                array[each_inner], array[each_inner + 1] = array[each_inner + 1], array[each_inner]
    
    return array


bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!