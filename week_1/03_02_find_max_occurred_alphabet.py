input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    # 이 부분을 채워보세요!
    occurred_array = [0] * 26
    print(occurred_array)
    for each in string :
        if each.isalpha() is not True :
            continue
        alpha_index = ord(each) - ord("a") 
        occurred_array[alpha_index] = occurred_array[alpha_index] + 1
    print(occurred_array)
    max_occur = 0
    max_alpha_index = 0

    for index in range(len(occurred_array)) :
        alpha_occur = occurred_array[index]
        if alpha_occur > max_occur :
            max_occur = alpha_occur
            max_alpha_index = index
    return chr(max_alpha_index + 97)

result = find_max_occurred_alphabet(input)
print(result)