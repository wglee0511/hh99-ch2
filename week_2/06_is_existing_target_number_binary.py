finding_target = 5
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_binary(target, array):
    cur_min_index = 0
    cur_max_index = len(array) - 1
    cur_guess = (cur_max_index + cur_min_index) // 2
    find_count = 0
    while cur_min_index <= cur_max_index:
        if array[cur_guess] == target :
            find_count += 1
            return True, find_count
        if array[cur_guess] < target :
            cur_min_index = cur_guess + 1        
        if array[cur_guess] > target :
            cur_max_index = cur_guess - 1
        find_count += 1
        cur_guess = (cur_max_index + cur_min_index) // 2
    return False, find_count

result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)