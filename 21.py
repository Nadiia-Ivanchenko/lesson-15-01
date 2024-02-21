def is_even(number):
    """
    Перевіряє, чи є число парним, без використання ділення.
    """
    binary_representation = bin(number)
    # Останній біт в бінарному представленні числа. Якщо він 0, число парне.
    last_bit = binary_representation[-1]
    return last_bit == '0'

# Тести
assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'
print('Ok')