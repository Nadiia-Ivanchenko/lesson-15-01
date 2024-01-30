def calculate_sum_and_multiply(arr):
    if not arr:
        return 0

    # Знаходимо суму елементів з парними індексами
    sum_of_even_index_elements = sum(arr[::2])

    # Знаходимо останній елемент масиву
    last_element = arr[-1]

    # Перемножуємо суму на останній елемент
    result = sum_of_even_index_elements * last_element

    return result

# Приклади використання:
arr1 = [0, 1, 7, 2, 4, 8]
result1 = calculate_sum_and_multiply(arr1)
print(result1)

