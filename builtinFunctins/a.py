import math

def multiply_numbers(numbers):
    result = math.prod(numbers)
    return result


numbers = [1, 2, 3, 4, 5]
result = multiply_numbers(numbers)
print("List:", numbers)
print("Result of multiplying all numbers:", result)