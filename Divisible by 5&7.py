def divisible_by_5_and_7(num):
    if num % 5 == 0 and num % 7 == 0:
        return True
    return False

# Sample Data
number = 35
result = divisible_by_5_and_7(number)
print(f"Is {number} divisible by both 5 and?{result}")