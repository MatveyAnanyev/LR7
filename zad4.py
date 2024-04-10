def is_prime(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    else:
        # Проверяем деление на числа от 3 до квадратного корня из числа
        for i in range(3, int(num**0.5) + 1, 2):
            if num % i == 0:
                return False
        return True

number = int(input("Введите целое число больше 1: "))

if is_prime(number):
    print(f"Число {number} является простым.")
else:
    print(f"Число {number} не является простым.")
