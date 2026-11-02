
# Читаем текст из файла
with open("input.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Разбиваем текст на слова
words = text.split()

# Создаем таблицу со списками
size = len(words) * 2 + 1
table = []

for i in range(size):
    table.append([])

# Добавляем слова в таблицу
for word in words:

    # Вычисляем хеш слова
    index = 0
    for char in word:
        index += ord(char)

    index = index % size

    table[index].append(word)

# Записываем таблицу в файл
with open("result14.txt", "w", encoding="utf-8") as file:
    for i in range(size):
        file.write(str(i) + ": " + str(table[i]) + "\n")

print("Готово! Результат записан в файл.")
