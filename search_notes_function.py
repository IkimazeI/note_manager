def search_notes(notes, keyword=None, status=None):
    # Проверка на пустой список заметок
    if not notes:
        print("Список заметок пуст.")
        return

    # Список для хранения найденных заметок
    found_notes = []

    for note in notes:
        # Проверяем совпадение по ключевым словам
        keyword_match = (keyword is None or
                         (keyword.lower() in note['title'].lower() or
                          keyword.lower() in note['content'].lower() or
                          keyword.lower() in note['username'].lower()))

        # Проверяем совпадение по статусу
        status_match = (status is None or
                        note['status'] == status)

        # Если оба условия выполняются, добавляем заметку в результаты
        if keyword_match and status_match:
            found_notes.append(note)

    # Вывод результатов
    if found_notes:
        print("Найдены заметки:")
        for i, note in enumerate(found_notes, start=1):
            print(f"Заметка №{i}:")
            print(f"Имя пользователя: {note['username']}")
            print(f"Заголовок: {note['title']}")
            print(f"Описание: {note['content']}")
            print(f"Статус: {note['status']}\n")
    else:
        print("Заметки, соответствующие запросу, не найдены.")

# Пример работы программы
notes = [
    {'username': 'Алексей', 'title': 'Список покупок',
     'content': 'Купить продукты на неделю', 'status': 'новая',
     'created_date': '27-11-2024', 'issue_date': '30-11-2024'},
    {'username': 'Мария', 'title': 'Учеба', 'content':
        'Подготовиться к экзамену', 'status': 'в процессе',
     'created_date': '25-11-2024', 'issue_date': '01-12-2024'},
    {'username': 'Иван', 'title': 'План работы', 'content':
        'Завершить проект', 'status': 'выполнено',
     'created_date': '20-11-2024', 'issue_date': '26-11-2024'}
]

# Вывод списка заметок при запуске
print("Список заметок:")
for i, note in enumerate(notes, start=1):
    print(f"Заметка №{i}:")
    print(f"Имя пользователя: {note['username']}")
    print(f"Заголовок: {note['title']}")
    print(f"Описание: {note['content']}")
    print(f"Статус: {note['status']}\n")

while True:
    print("\nВведите параметры для поиска заметок.")
    keyword = input("Введите ключевое слово (или оставьте пустым для поиска по статусу): ")
    status = input("Введите статус (или оставьте пустым для поиска по ключевым словам): ")

    if not keyword and not status:
        print("Оба поля пусты. Попробуйте снова.")
        continue

    search_notes(notes, keyword if keyword else None or status if status else None)

    # Запрос на продолжение поиска
    continue_search = input("Хотите продолжить поиск? (да/нет): ").strip().lower()
    if continue_search != 'да':
        break