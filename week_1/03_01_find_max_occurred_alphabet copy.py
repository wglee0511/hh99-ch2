input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    # 이 부분을 채워보세요!
    alpha_arr = []
    for each in range(97, 97+26) :
        alpha_arr.append(chr(each))
    
    max_occur = 0
    max_alpha = alpha_arr[0]

    for each in alpha_arr :
        occur = 0
        for each_str in string :
            if each == each_str :
                occur += 1
            if max_occur < occur :
                max_occur = occur
                max_alpha = each_str
    
    return max_alpha


result = find_max_occurred_alphabet(input)
print(result)