def find_pairs(nums, target):
    seen = set()
    print(f"Pairs with sum {target}:")

    for num in nums:
        complement = target - num
        if complement in seen:
            print(f"({complement}, {num})")
        seen.add(num)


# Sample Input
numbers = [10, 20, 30, 40, 50, 60]
target = 100

find_pairs(numbers, target)
