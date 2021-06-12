input = 20


def find_prime_list_under_number(number):
    num_arr = []
    if number > 2 :
        for each in range(2, number + 1) :
            confirm_num = 0
            for each_innner in range(2, each) :
                if each % each_innner == 0 :
                    confirm_num = 1
                    break
            if confirm_num == 0 :
                num_arr.append(each)
                    
    else : 
        return "non prime number"

    return num_arr


result = find_prime_list_under_number(input)
print(result)