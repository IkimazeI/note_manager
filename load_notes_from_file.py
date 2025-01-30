import os
from logging import exception


def create_default_note_file(filename):
    # заглушка на случай, если файла нет или он пустой
    default_content = """Имя пользователя: Алексей
Заголовок: Список покупок
Описание: Купить продукты
Статус: новая
Дата создания: 27-11-2024
Дедлайн: 30-11-2024
"""
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(default_content.strip())

def read_notes_from_file(filename):
    # проверка файла на существование и заполненность
    try:
        if not os.path.exists(filename) or os.path.getsize(filename) == 0:
            create_default_note_file(filename)

        notes = []
        note = {}

        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                # сносим пробелы и перевод строки
                line = line.strip()
                # скипаем пустые строки
                if not line:
                    continue

                # прямое присвоение в зависимости от порядка строк
                if line.startswith("Имя пользователя:"):
                    note['username'] = line.split(': ', 1)[1]
                elif line.startswith("Заголовок:"):
                    note['title'] = line.split(': ', 1)[1]
                elif line.startswith("Описание:"):
                    note['content'] = line.split(': ', 1)[1]
                elif line.startswith("Статус:"):
                    note['status'] = line.split(': ', 1)[1]
                elif line.startswith("Дата создания:"):
                    note['created_date'] = line.split(': ', 1)[1]
                elif line.startswith("Дедлайн:"):
                    note['issue_date'] = line.split(': ', 1)[1]

            # добавляем заметку в список, если она не пустая
            if note:
                notes.append(note)

        return notes
    except FileNotFoundError:
        print('Файл filename не найден. Создан новый файл.')
    except:
        print('Ошибка при чтении файла filename. Проверьте его содержимое.')

filename = 'filename.txt'
result = read_notes_from_file(filename)
print(result)