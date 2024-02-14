def difference(*args):
    # Перевірка, чи є аргументи
    if not args:
        return 0

    # Знаходження максимуму та мінімуму серед аргументів
    max_value = max(args)
    min_value = min(args)

    # Обчислення різниці
    result = max_value - min_value

    # Округлення результату до двох знаків після коми
    result = round(result, 2)

    return result


# Перевірка прикладів
assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')