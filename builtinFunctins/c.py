def is_palindrome(string):
    reversed_string = string[::-1]
    
    return string == reversed_string

string = "radar"
result = is_palindrome(string)
if result:
    print(string, "is a palindrome.")
else:
    print(string, "is not a palindrome.")