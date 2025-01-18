import re
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


def update_note(note):
    # показываем юзеру текущие данные заметки
    print("Текущие данные заметки:")
    print(note)

    # доступные поля для обновления
    fields = ['username', 'title', 'content', 'status', 'issue_date']

    # запрос на выбор поля для обновления
    while True:
        field_to_update = input(f"Какие данные вы хотите обновить? ({', '.join(fields)}): ")
        if field_to_update in fields:
            break
        else:
            print("Некорректное имя поля! Пожалуйста, выберите одно из предложенных полей.")

    # блок выполнения перезаписи значения
    if field_to_update == 'issue_date':
        date_pattern = r"^\d{2}-\d{2}-\d{4}$"
        while True:
            new_value = input(f"Введите новое значение для {field_to_update}: ")
            if re.match(date_pattern, new_value):
                day, month, year = map(int, new_value.split('-'))
                # проверка корректности даты
                if (1 <= day <= 31 and 1 <= month <= 12 and
                        ((month == 2 and day <= 29) or
                         (month in [4, 6, 9, 11] and day <= 30) or
                         (month != 2 and day <= 31))):
                    break
            print("Неверный формат даты! Пожалуйста, используйте день-месяц-год.")
    else:
        new_value = input(f"Введите новое значение для {field_to_update}: ")

    # обновляем поле заметки
    note[field_to_update] = new_value

    return note


if __name__ == "__main__":
    note = create_note()

    # обновляем заметку
    updated_note = update_note(note)
    print("Заметка обновлена:")
    print(updated_note)