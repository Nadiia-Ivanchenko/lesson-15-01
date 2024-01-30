def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

while True:
    # Введення чисел та операції користувачем
    num1 = float(input("Введіть перше число: "))
    operator = input("Введіть операцію (+, -, *, /): ")
    num2 = float(input("Введіть друге число: "))

    # Обчислення та виведення результату
    if operator == "+":
        result = add(num1, num2)
    elif operator == "-":
        result = subtract(num1, num2)
    elif operator == "*":
        result = multiply(num1, num2)
    elif operator == "/":
        result = divide(num1, num2)
    else:
        result = "Невідома операція"

    print("Результат: ", result)

    # Запитання користувача про продовження
    user_input = input("Бажаєте продовжити? (y/n): ")
    if user_input.lower() != 'y':
        break