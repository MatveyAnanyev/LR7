number = int(input("Введите число для таблицы умножения: "))

print(f"Таблица умножения для числа {number}:")

for i in range(1, 11):
    result = number * i
    print(f"{number} * {i} = {result}")