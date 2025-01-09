# устанавливаем статус заметки в словаре
note_data = {"status": "в процессе"}

# показываем текущий статус
print(f'Текущий статус заметки: "{note_data["status"]}"')

# вывод доступных статусов пользователю
statuses = ["выполнено", "в процессе", "отложено"]
print("\nВыберите новый статус заметки или введите его текстом:")
i = 3
g = 0
for i in statuses:
    print(f"{g+1}. {statuses[g]}")
    g+=1

while True:
    choice = input("\nВаш выбор: ").strip().lower()

    # проверка ввода числа
    if choice.isdigit():
        choice_num = int(choice)
        if 1 <= choice_num <= len(statuses):
            note_data["status"] = statuses[choice_num - 1]
            break
    # проверка текстового ввода (долго ломал голову, почему нет else if, а оно в таком виде)
    elif choice in statuses:
        note_data["status"] = choice
        break

    print("Некорректный ввод. Попробуйте снова.")

# обновлённый статус
print(f'\nСтатус заметки успешно обновлён на: "{note_data["status"]}"')