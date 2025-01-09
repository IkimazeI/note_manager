from datetime import datetime

created_date = datetime.now()
issue_date = input('\nВведите дату окончания заметки в формате 31-12-2025: ')

print('Дата создания заметки:', created_date.strftime("%d-%m"))
print('Дата окончания срока заметки:', issue_date[0:5])
