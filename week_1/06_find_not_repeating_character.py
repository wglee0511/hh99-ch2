input = "aauaddedccfffg"

def find_not_repeating_character(string):
    alpha_arr = [0] * 26
    for each in string :
        alpha_num = ord(each) - 97
        alpha_arr[alpha_num] = alpha_arr[alpha_num] + 1

    for each in string :
        each_index = ord(each) - 97
        if alpha_arr[each_index] == 1 :
            return chr(each_index + 97)




result = find_not_repeating_character(input)
print(result)