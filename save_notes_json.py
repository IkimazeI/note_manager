import json

def save_notes_json(notes, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(notes, f, ensure_ascii=False, indent=4)
        print(f"Заметки успешно сохранены в {filename}")
    except Exception as e:
        print(f"Произошла ошибка при сохранении заметок: {e}")

notes = [
    {
        "username": "Алексей",
        "title": "Список покупок",
        "content": "Купить продукты",
        "status": "новая",
        "created_date": "27-11-2024",
        "issue_date": "30-11-2024"
    }
]

save_notes_json(notes, 'notes.json')