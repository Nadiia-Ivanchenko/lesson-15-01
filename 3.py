# Введення першого числа
num1 = float(input("Введіть перше число: "))

# Введення операції
operation = input("Введіть операцію (+, -, *, /): ")

# Введення другого числа
num2 = float(input("Введіть друге число: "))

# Обчислення та виведення результату
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    # Перевірка на ділення на 0
    if num2 == 0:
        print("Помилка: Ділення на 0 неможливе.")

    else:
        result = num1 / num2
else:
    print("Помилка: Непідтримувана операція.")


print("Результат:", result)