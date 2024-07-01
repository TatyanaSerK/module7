def custom_write(file_name, strings):
    strings_positions = {}  # пустой словарь
    num_line = 0
    file = open(file_name, mode='w', encoding='utf-8')  # файла для записи
    for i in strings:
        num_line += 1  # номер строки от 1
        num_byte = file.tell()  # байт начала строки
        file.write(f'{i}\n')  # записывать все строки из списка, каждая на новой строке
        a = (num_line, num_byte)  # кортеж (номер строки, байт начала строки)
        strings_positions[a] = i  # создаем словарь
    file.close()  # закрыть файл
    return strings_positions  # возвращаем словарь



info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', strings=info)
for elem in result.items():
    print(elem)
