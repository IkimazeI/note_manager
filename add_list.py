# в начале код по ТЗ, далее мой для развития
headers = []

header1 = input("Введите первый заголовок: ")
headers.append(header1)
header2 = input("Введите второй заголовок: ")
headers.append(header2)
header3 = input("Введите третий заголовок: ")
headers.append(header3)

print(headers)










# # создание списка для хранения заголовков
# header = []
#
# # переменная, отвечающая за количество заголовков в заметке
# headers = input("Сколько заголовков у Вас будет? ")
#
# # цикл, считающий количество заголовков, которые указал пользователь и предлагающий ввести имя для каждого
# for count in range(int(headers)):
#     # здесь как раз и вводится название для каждого заголовка
#     header_count = input(f"Введите {count+1}-й заголовок для заметки: ")
#     # прибавление к списку заголовка
#     header.append(header_count)
#
# # сортировка списка
# header.sort()
#
# # цикл, чтобы вывести все заголовки
# for i in range(int(headers)):
#     print(header[i] + "\r")