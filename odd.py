def is_odd_and_not_divisible_by_3(number):
    if number % 2 != 0 and number % 3 != 0:  # Check if odd and not divisible by 3
        return True
    return False

# Test the function
numbers = [27, 15, 11, 7, 30, 19]
for num in numbers:
    result = is_odd_and_not_divisible_by_3(num)
    print(f"Number: {num}, Is odd and not divisible by3?{result}")