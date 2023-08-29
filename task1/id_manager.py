from zipfile import ZipFile

# Создаем пустой словарь в который будем добавлять id и количество повторений
id_dict = {}

# Создаем отдельную переменную для названия файла
name_zip_file = 'ea81acbe06c3c56f4416fc0b1fc36837069f69dd08b22271366d2acf898d59f2.zip'

# Проверка есть ли файл .zip
try:
    with ZipFile(name_zip_file) as zip_file:
        # Читаем zip архив
        file_name = zip_file.namelist()[0]
        # Проверяем есть ли файл csv
        if not file_name.endswith('.csv'):
            print('В архиве нет файла формата csv')
            exit()

        # Читаем csv файл
        with zip_file.open(file_name) as file:
            data = file.read().decode('utf-8', errors='ignore')
            # Из каждой строчки добавляем в словарь id и добавляем количество повторений в значение
            for line in data.splitlines():
                # Проверяем на соответствие заданному формату
                try:
                    id_dict[line.split(',')[1]] = id_dict.get(line.split(',')[1], 0) + 1
                except IndexError:
                    print('Файл не соответствует формату таблицы со столбами cache, id')
                    exit()

# Если файла нет, то выводится ошибка
except FileNotFoundError:
    print('Такого файла нет')

# Задаем максимальное значение
max_value = 0
# Перебираем словарь и устанавливаем максимальное значение и выводим id, если они повторялись 3 раза
for key, value in id_dict.items():
    if value > max_value:
        max_value = value
    if value == 3:
        print(key)

# Добавляем пустую строчку между выводами и выводим список повторений с 1 раза по max_value
print()
for i in range(1, max_value + 1):
    print(f"Количество повторений {i} раз: {list(id_dict.values()).count(i)}")
