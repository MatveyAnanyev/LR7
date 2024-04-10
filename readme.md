# Лабораторная работа №7. Решение алгоритмических задач с применением циклов и ветвлений.
## Практическая часть.
1. Проверка на четность/нечетность: Запросите у пользователя целое число и определите, является ли оно четным или нечетным. Выведите соответствующее сообщение.
2. Поиск максимума: Попросите пользователя ввести три числа. Найдите и выведите максимальное из них, используя условный оператор.
3. Факториал числа: Запросите у пользователя целое неотрицательное число и вычислите его факториал. Факториал числа n, вычисляется как n! = 1 × 2 × 3 × … × n.
4. Проверка на простоту: Попросите пользователя ввести целое число больше 1. Определите, является ли это число простым (т.е., делится только на себя и на 1).
5. Таблица умножения: Выведите таблицу умножения от 1 до 10 для заданного пользователем числа.
6. Палиндром: Проверьте, является ли введенная пользователем строка палиндромом (читается одинаково как слева направо, так и справа налево, игнорируя пробелы, знаки препинания и регистр).
7. Подсчет гласных и согласных: Попросите пользователя ввести строку. Посчитайте количество гласных и согласных букв в этой строке.
8. Сумма элементов списка: Создайте список чисел. Вычислите и выведите сумму всех элементов списка.
9. Обратный порядок чисел: Запросите у пользователя натуральное число n. Выведите все числа от n до 1 в обратном порядке.

## Ответы на контрольные вопросы
**1. Что из себя представляют ветвления в python, какие конструкции языка используются?
***Ответ:*** Ветвление это операция, применяющаяся в случаях, когда выполнение или невыполнение некоторого набора команд должно зависеть от выполнения или невыполнения некоторого условия. if логическое_выражение { выражение 1; выражение 2; … } else { выражение 3 … }
**2. Что из себя представляют циклы в python, какие конструкции языка используются? В чем их отличие?
***Ответ:*** Циклы позволяют выполнять некоторое действие в зависимости от соблюдения некоторого условия. В языке Python есть следующие типы циклов: while и for. Цикл while проверяет истинность некоторого условия, и если условие истинно, то выполняет инструкции цикла.  for пробегается по набору значений, помещает каждое значение в переменную, и затем в цикле мы можем с этой переменной производить различные действия.
**3. Что из себя представляют списки, кортежи, словари?
***Ответ:***  Список (list) представляет тип данных, который хранит набор или последовательность элементов. Словарь (dictionary) в языке Python хранит коллекцию элементов, где каждый элемент имеет уникальный ключ и ассоциированое с ним некоторое значение. Кортеж (tuple) представляет последовательность элементов, которая во многом похожа на список за тем исключением, что кортеж является неизменяемым (immutable) типом. Поэтому мы не можем добавлять или удалять элементы в кортеже, изменять его.