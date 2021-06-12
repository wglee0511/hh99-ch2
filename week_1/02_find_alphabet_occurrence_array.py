def find_alphabet_occurrence_array(string):
    occurred_array = [0] * 26
    for each in string :
        if each.isalpha() is not True :
            continue
        alpha_index = ord(each) - ord("a")
        occurred_array[alpha_index] = occurred_array[alpha_index] + 1
    
    return occurred_array

print(find_alphabet_occurrence_array("hello my name is sparta"))