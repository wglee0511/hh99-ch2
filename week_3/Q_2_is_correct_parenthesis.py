s = ")(())()("


def is_correct_parenthesis(string):
    to_list = []

    for each in string :
        to_list.append(each)
    
    max_len_index = len(to_list) - 1

    return to_list[0] == "(" and to_list[max_len_index] == ")"


print(is_correct_parenthesis(s))  # True 를 반환해야 합니다!