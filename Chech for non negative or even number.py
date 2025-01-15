def check_number(num):
    if num >= 0 or num % 2 == 0:
        return True
    else:
        return False

# Sample data
num = -8
if check_number(num):
    print(f"{num} is either non-negative or even.")
else:
    print(f"{num} is neither non-negativenoreven.")