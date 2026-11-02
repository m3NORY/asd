
# Читаем текст из файла
with open("input.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Разбиваем текст на слова
words = text.split()

# Создаем пустую таблицу
size = len(words) * 2 + 1
table = [None] * size

# Добавляем слова в таблицу
for word in words:

    # Вычисляем хеш слова
    index = 0
    for char in word:
        index += ord(char)

    index = index % size

    # Ищем свободную ячейку
    while table[index] is not None:
        index = (index + 1) % size

    table[index] = word

# Записываем таблицу в файл
with open("result13.txt", "w", encoding="utf-8") as file:
    for i in range(size):
        file.write(str(i) + ": " + str(table[i]) + "\n")

print("Готово! Результат записан в файл.")
