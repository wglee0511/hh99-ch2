finding_target = 2
finding_numbers = [0, 3, 5, 6, 1, 2, 4]

def is_exist_target_number_binary(target, numbers):
    numbers.sort()
    min_index = 0
    max_index = len(numbers) - 1
    guess = (min_index + max_index) // 2

    while min_index <= max_index :
        if numbers[guess] == target :
            return True
        if numbers[guess] < target :
            min_index = guess + 1
        if numbers[guess] > target :
            max_index = guess - 1
        guess = (min_index + max_index) // 2

    return False


result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)