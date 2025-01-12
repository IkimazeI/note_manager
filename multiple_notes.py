from datetime import datetime

# список для хранения заметок
notes = []

print("Добро пожаловать в 'Менеджер заметок'! Вы можете добавить новую заметку.")

while True:
    # аргументы для заметки
    note = {'username': input('Введите имя пользователя: '),
            'title': input('Введите заголовок заметки: '),
            'content': input('Введите описание заметки: '),
            'status': input('Введите статус заметки (выполнено, ожидание, не выполнено): '),
            'creation_date': datetime.now().strftime("%d-%m"),
            'deadline': input('Введите дату истечения срока заметки: (день-месяц-год): ')}

    # добавление заметки в список
    notes.append(note)

    # добавление новой заметки
    another_note = input("Хотите добавить ещё одну заметку? (да/нет): ").strip().lower()
    if another_note != 'да':
        break

# все заметки
if not notes:
    print("Список заметок пуст.")
else:
    print("\nСписок заметок:")
    for index, note in enumerate(notes, start=1):
        print(f"{index}. Имя: {note['username']}")
        print(f"   Заголовок: {note['title']}")
        print(f"   Описание: {note['content']}")
        print(f"   Статус: {note['status']}")
        print(f"   Дата создания: {note['creation_date']}")
        print(f"   Дедлайн: {(note['deadline'][0:5])}\n")