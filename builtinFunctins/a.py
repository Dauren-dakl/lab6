def multiply_numbers(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

num_list = [2, 3, 4, 5]
result = multiply_numbers(num_list)
print("answer:", result)