titles = []

while True: # Выполняется, пока ввод не будет пустым
    title = input("Введите заголовок (или оставьте пустым для завершения): ")

    if title == '': # Проверка, завершил ли ввод пользователь (нажал Enter)
        break

    if title.strip(): # Проверка на пустые заголовки
        if title in titles: # Проверка на уникальность заголовков
            print("Этот заголовок уже есть ;)")
        else:
            titles.append(title)

print("Заголовки заметки:")
for title in titles:
    print("- " + title)