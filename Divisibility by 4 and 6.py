
def check_divisibility(number):
    if number % 4 == 0 or number % 6 == 0:
        return f"{number} is divisible by 4 or 6."
    else:
        return f"{number} is not divisible by 4 or 6."
number = 18
print(check_divisibility(number))