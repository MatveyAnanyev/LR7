def count_vowels_consonants(s):
    # Приводим строку к нижнему регистру для удобства подсчета
    s = s.lower()
    vowels = 0
    consonants = 0
    # Задаем множества гласных и согласных букв
    vowel_set = set("aeiou")
    consonant_set = set("bcdfghjklmnpqrstvwxyz")
    # Подсчитываем количество гласных и согласных букв в строке
    for char in s:
        if char in vowel_set:
            vowels += 1
        elif char in consonant_set:
            consonants += 1
    return vowels, consonants

string = input("Введите строку: ")

vowels, consonants = count_vowels_consonants(string)

print(f"Количество гласных букв: {vowels}")
print(f"Количество согласных букв: {consonants}")