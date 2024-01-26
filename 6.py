def move_zeros_to_end(lst):
    non_zeros = [num for num in lst if num != 0]
    zeros = [0] * (len(lst) - len(non_zeros))
    result = non_zeros + zeros
    lst[:] = result

# Приклади використання:
list1 = [0, 1, 0, 12, 3]
move_zeros_to_end(list1)
print(list1)