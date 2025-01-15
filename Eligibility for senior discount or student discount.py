
def check_discount(age):
    if age > 60:
        return "Eligible for Senior Citizen Discount"
    elif age < 25:
        return "Eligible for Student Discount"
    else:
        return "Not eligible for any discount"
age = 63
print(check_discount(age))