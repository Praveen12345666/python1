def check_eligibility(age):
    if age >= 18:
        print(f"Age {age}: Eligible to vote.")
    else:
        print(f"Age {age}: Not eligible to vote.")

    if age >= 16:
        print(f"Age {age}: Eligible to drive.")
    else:
        print(f"Age {age}: Not eligible to drive.")


# Test the function with age 20
age = 20
check_eligibility(age)