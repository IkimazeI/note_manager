from datetime import datetime

# список для хранения заметок
notes = []

print("Добро пожаловать в 'Менеджер заметок'! Вы можете добавить новую заметку.")

while True:
    # аргументы для заметок
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

# операция удаления заметки
while True:
    delete_criteria = input(
        "Введите имя пользователя или заголовок для удаления заметки (или 'стоп' для завершения): ").strip()
    if delete_criteria.lower() == 'стоп':
        break

    # берёт значение количества заметок
    original_length = len(notes)

    '''
    [note for note in notes~]
    перебирает все элементы (note) в исходном списке notes
    
    if note['username'] != delete_criteria and note['title'] != delete_criteria 
    условие фильтрации проверяет, не равны ли имя пользователя (note['username']) и 
    заголовок (note['title']) введенному критерию удаления (delete_criteria)
    
    оба условия должны быть истинны, чтобы заметка была отобрана условием, 
    потому что используется оператор and, 
    который является строгим оператором, в отличии от or
    '''
    notes = [note for note in notes if note['username']
             != delete_criteria and note['title'] != delete_criteria]

    if len(notes) < original_length:
        print("Успешно удалено.")

        # поскорее бы изучить классы, чтобы не писать 2 раза один и тот же код...)

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
    else:
        print("Заметок с таким именем пользователя или заголовком не найдено.")




