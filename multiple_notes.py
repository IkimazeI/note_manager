from datetime import datetime
from time import sleep

note_value = []

date_creation = datetime.now()

count_notes = 0

while True:
    note_value.clear()
    count_notes+=1
    username = input('Введите имя пользователя: ')
    note_value.append(username)
    header = []
    headers = input('Сколько заголовков у Вас будет? ')
    for count in range(int(headers)):
        header_count = input(f'Введите {count+1}-й заголовок для заметки: ')
        header.append(header_count)
    header.sort()
    note_value.append(header)
    content = input('Введите содержимое заметки: ')
    note_value.append(content)
    status = input('Введите статус заметки (выполнено, ожидание, не выполнено): ')
    note_value.append(status)
    issue_date = input('Введите дату истечения срока заметки: ')
    note_value.append(issue_date)

    short_date = note_value[4]

    print(f"Заметка № {count_notes}")
    print("\nДанные о заметке:")
    print("Имя пользователя:", note_value[0])
    print("Заголовки:", note_value[1])
    print("Содержание заметки:", note_value[2])
    print("Дата создания:", date_creation.strftime("%d-%m"))
    print("Статус заметки:", note_value[3])
    print("Дата истечения срока заметки:", short_date[0:5])
    sleep(1)
    choice = input("Желаете добавить ещё одну заметку? (да/нет): ").strip().lower()
    if choice == "нет":
        break