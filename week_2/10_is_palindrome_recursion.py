input = "asdzxa"


def is_palindrome(string):
    if len(string) == 0 :
        return True
    if string[0] != string[-1] :
        return False
    return is_palindrome(string[1:-1])



print(is_palindrome(input))