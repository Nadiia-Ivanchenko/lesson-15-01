def find_unique_value(some_list):
    unique_values = set()
    duplicate_values = set()

    for num in some_list:
        if num not in duplicate_values:
            if num in unique_values:
                unique_values.remove(num)
                duplicate_values.add(num)
            else:
                unique_values.add(num)

    return unique_values.pop()

# Тести
assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")