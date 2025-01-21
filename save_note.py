from datetime import datetime


def save_notes_to_file(notes, filename):
    '''
    Почитал про with, потому что думал, что файл нужно создавать вручную, если его не существует.
    При использовании данной конструкции в коде, не придётся пользоваться file.close(),
    как говорится в занятии, поэтому я использовал это
    '''
    with open(filename, 'w', encoding='utf-8') as file:
        for note in notes:
            created_date = datetime.now().strftime('%d-%m-%Y')
            note_content = (
                f"Имя пользователя: {note['username']}\n"
                f"Заголовок: {note['title']}\n"
                f"Описание: {note['content']}\n"
                f"Статус: {note['status']}\n"
                f"Дата создания: {created_date}\n"
                f"Дедлайн: {note['issue_date']}\n"
                f"--------------------------------------\n"
            )
            # запись заметки в файл
            file.write(note_content)


def input_notes():
    notes = []
    while True:
        username = input("Введите имя пользователя (или оставьте пустым для завершения): ")
        if not username:
            break
        title = input("Введите заголовок заметки: ")
        content = input("Введите описание заметки: ")
        status = input("Введите статус заметки: ")
        issue_date = input("Введите дедлайн заметки: ")

        note = {
            'username': username,
            'title': title,
            'content': content,
            'status': status,
            'issue_date': issue_date
        }
        notes.append(note)

    return notes


if __name__ == "__main__":
    # заметки от пользователя
    user_notes = input_notes()
    # сохранение заметок в файл
    save_notes_to_file(user_notes, 'notes.txt')