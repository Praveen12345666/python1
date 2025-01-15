def check_range(num):
    if (1 <= num <= 10) or (20 <= num <= 30):
        return True
    return False

# Test the function
number = 25
print(f"Number: {number} in range: {check_range(number)}")