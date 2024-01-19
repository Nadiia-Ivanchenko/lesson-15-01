# Запит користувача на введення 4-х значного числа
user_input = input("Введіть 4-х значне число: ")

# Перевірка, чи введено рівно 4 символи
if len(user_input) == 4 and user_input.isdigit():
    # Розділення числа на цифри та виведення їх по одній
    print(int(user_input) // 1000)
    print((int(user_input) // 100) % 10)
    print((int(user_input) // 10) % 10)
    print(int(user_input) % 10)