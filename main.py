def calculator():
    num1 = float(input("Перше число: "))
    operation = input("Операція: ")
    num2 = float(input("Друге число: "))

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '/':
        # Перевіряємо, щоб не було ділення на 0. Видасть помилку.
        if num2 != 0:
            result = num1 / num2
        else:
            print("Ділення на нуль неможливе.")
            return

    elif operation == '*':
        result = num1 * num2
    elif operation == 'mod':
        result = num1 % num2
    elif operation == 'pow':
        result = num1 ** num2
    elif operation == 'div':
        # Перевіряємо, щоб не було ділення на 0. Буде помилка.
        if num2 != 0:
            result = num1 // num2
            print("Ділення на нуль неможливе.")
            return
    else:
        print("Непідтримувана операція")
        return

    print("Результат:", result)

calculator()
