def check_negative_and_odd(num):
    if num < 0 and num % 2 != 0:
        return True
    return False

# Test the function
number = -7
print(f"Number: {number} is negative and odd: {check_negative_and_odd(number)}")