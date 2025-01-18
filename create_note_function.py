from datetime import datetime

# используем функцию для удобства
def create_note():
    username = input("Введите имя пользователя: ")
    title = input("Введите заголовок заметки: ")
    content = input("Введите описание заметки: ")
    status = input("Введите статус заметки (новая, в процессе, выполнена): ")

    # получаем текущую дату
    created_date = datetime.now().strftime("%d-%m-%Y")

    # запрашиваем дату дедлайна и проверяем формат
    while True:
        issue_date = input("Введите дату дедлайна (день-месяц-год): ")
        try:
            datetime.strptime(issue_date, "%d-%m-%Y")
            break
        except ValueError:
            print("Неверный формат даты! Пожалуйста, используйте день-месяц-год.")

    # словарь с данными заметки
    note = {
        'username': username,
        'title': title,
        'content': content,
        'status': status,
        'created_date': created_date,
        'issue_date': issue_date
    }

    return note


# вызов функции и вывод результата
if __name__ == "__main__":
    note = create_note()
    print("Заметка создана:", note)