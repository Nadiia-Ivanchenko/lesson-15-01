import string
import keyword


def is_valid_variable_name(variable_name):
    # Перевірка чи починається змінна з літери або підкреслення
    if not (variable_name[0].isalpha() or variable_name[0] == '_'):
        return False

    # Перевірка решти символів
    for char in variable_name[1:]:
        if char not in string.ascii_letters + string.digits + '_':
            return False

    # Перевірка чи не є ім'ям змінної зарезервоване слово
    if variable_name in keyword.kwlist:
        return False

    return True


# Приклади використання:
print(is_valid_variable_name("_"))  # Виведе: True
print(is_valid_variable_name("x"))  # Виведе: True
print(is_valid_variable_name("get_value"))  # Виведе: True
print(is_valid_variable_name("get value"))  # Виведе: False
print(is_valid_variable_name("get!value"))  # Виведе: False
print(is_valid_variable_name("some_super_puper_value"))  # Виведе: True
print(is_valid_variable_name("Get_value"))  # Виведе: False
print(is_valid_variable_name("get_Value"))  # Виведе: False
print(is_valid_variable_name("getValue"))  # Виведе: False
print(is_valid_variable_name("3m"))  # Виведе: False
print(is_valid_variable_name("m3"))  # Виведе: True