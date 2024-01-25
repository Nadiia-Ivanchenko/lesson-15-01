def move_last_to_first(lst):
    if len(lst) > 1:
        last_element = lst.pop()
        lst.insert(0, last_element)

# Приклади використання:
list1 = [12, 3, 4, 10]
move_last_to_first(list1)
print(list1)
