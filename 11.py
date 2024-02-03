

# Задані словники
my_dict_1 = {1: 1, 2: 2}
my_dict_2 = {11: 11, 2: 22}

# а) Створити список із ключів, які є в обох словниках.
common_keys = list(set(my_dict_1.keys()) & set(my_dict_2.keys()))

# б) Створити список із ключів, які є у першому, але немає у другому словнику.
keys_only_in_first = list(set(my_dict_1.keys()) - set(my_dict_2.keys()))

# в) Створити новий словник з пар {ключ:значення} для ключів, які є в першому, але немає в другому словнику.
new_dict = {key: my_dict_1[key] for key in keys_only_in_first}

# г) Об'єднати ці два словники у новий словник за правилом:
# якщо ключ є тільки в одному з двох словників - помістити пару ключ: значення,
# якщо ключ є у двох словниках - помістити пару {ключ: [значення_з_першого_словника, значення_з_другого_словника]}.

merged_dict = {}

for key in set(my_dict_1.keys()) | set(my_dict_2.keys()):
    if key in my_dict_1 and key in my_dict_2:
        merged_dict[key] = [my_dict_1[key], my_dict_2[key]]
    elif key in my_dict_1:
        merged_dict[key] = my_dict_1[key]
    elif key in my_dict_2:
        merged_dict[key] = my_dict_2[key]

print("а) Список із ключів, які є в обох словниках:", common_keys)
print("б) Список із ключів, які є у першому, але немає у другому словнику:", keys_only_in_first)
print("в) Новий словник з пар {ключ:значення} для ключів, які є в першому, але немає в другому словнику:", new_dict)
print("г) Об'єднаний словник:", merged_dict)