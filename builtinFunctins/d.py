import time
import math

def delayed_square_root(number, milliseconds):
    time.sleep(milliseconds / 1000)  
    result = math.sqrt(number)
    return result

number = 25100
milliseconds = 2123


result = delayed_square_root(number, milliseconds)


print(f"Square root of {number} after {milliseconds} milliseconds is {result}")