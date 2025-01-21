import datetime


def create_note():
    username = input("Введите ваше имя: ")
    title = input("Введите заголовок заметки: ")
    content = input("Введите текст вашей новой заметки: ")
    status = input("Введите статус заметки (новая, в процессе, выполнено): ")
    created_date = datetime.date.today().strftime("%d-%m-%Y")
    issue_date = input("Введите дедлайн заметки (дд-мм-гггг): ")

    note = {
        'username': username,
        'title': title,
        'content': content,
        'status': status,
        'created_date': created_date,
        'issue_date': issue_date
    }
    notes.append(note)
    print("Новая заметка создана!")


def display_notes():
    if notes:
        print("Список всех заметок:")
        for i, note in enumerate(notes, start=1):
            print(f"Заметка №{i}. Имя: {note['username']}\n"
                  f"            Заголовок: {note['title']}\n"
                  f"            Описание: {note['content']}\n"
                  f"            Дата создания: {note['created_date']}\n"
                  f"            Дедлайн: {note['issue_date']}\n"
                  f"            Статус: {note['status']}")
    else:
        print("Нет доступных заметок.")


def update_note():
    display_notes()
    if notes:
        note_index = int(input("Введите номер заметки для обновления: ")) - 1
        if 0 <= note_index < len(notes):
            new_content = input("Введите новое описание заметки: ")
            notes[note_index]['content'] = new_content
            print("Заметка обновлена!")
        else:
            print("Некорректный номер заметки.")


def delete_note():
    display_notes()
    if notes:
        note_index = int(input("Введите номер заметки для удаления: ")) - 1
        if 0 <= note_index < len(notes):
            notes.pop(note_index)
            print("Заметка удалена!")
        else:
            print("Некорректный номер заметки.")


def search_notes():
    query = input("Введите текст для поиска в содержимом заметок: ")
    found_notes = [note for note in notes if query in note['content']]

    if found_notes:
        print("Найденные заметки:")
        for i, note in enumerate(found_notes, start=1):
            print(f"Заметка №{i}. Имя: {note['username']}\n"
                  f"            Заголовок: {note['title']}\n"
                  f"            Описание: {note['content']}\n"
                  f"            Дата создания: {note['created_date']}\n"
                  f"            Дедлайн: {note['issue_date']}\n"
                  f"            Статус: {note['status']}")
    else:
        print("Заметки не найдены.")


notes = [
    {'username': 'Алексей', 'title': 'Список покупок', 'content': 'Купить продукты на неделю', 'status': 'новая',
     'created_date': '27-11-2024', 'issue_date': '30-11-2024'},
    {'username': 'Мария', 'title': 'Учеба', 'content': 'Подготовиться к экзамену', 'status': 'в процессе',
     'created_date': '25-11-2024', 'issue_date': '01-12-2024'},
    {'username': 'Иван', 'title': 'План работы', 'content': 'Завершить проект', 'status': 'выполнено',
     'created_date': '20-11-2024', 'issue_date': '26-11-2024'}
]


def menu():
    while True:
        print("\nМеню действий:")
        print("1. Создать новую заметку")
        print("2. Показать все заметки")
        print("3. Обновить заметку")
        print("4. Удалить заметку")
        print("5. Найти заметки")
        print("6. Выйти из программы")

        choice = input("Ваш выбор: ")

        if choice == '1':
            create_note()
        elif choice == '2':
            display_notes()
        elif choice == '3':
            update_note()
        elif choice == '4':
            delete_note()
        elif choice == '5':
            search_notes()
        elif choice == '6':
            print("Программа завершена. Спасибо за использование!")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите действие из списка.")


if __name__ == "__main__":
    menu()