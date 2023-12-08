import csv
import json

# Початок частини Колпакова Михайла
csv_data = [
    {"Ім'я": "Михайло", "Прізвище": "Колпаков", "Вік": 19, "День народження": "23.03.04"}
]

csv_filename = "data.csv"
json_filename = "data.json"

try:
    # Запис у csv файл
    with open(csv_filename, 'w', newline = '', encoding = 'utf-8') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames = csv_data[0].keys())
        csv_writer.writeheader()
        csv_writer.writerows(csv_data)
        
    # Конвертація у json файл
    with open(csv_filename, 'r', newline = '', encoding = 'utf-8') as csv_file:
        csv_data = list(csv.DictReader(csv_file))
        
    # Запис у json файл
    with open(json_filename, 'w', encoding = 'utf-8') as json_file:
        json.dump(csv_data, json_file, ensure_ascii = False, indent = 2)
        
except Exception as e:
    print(f'Виникла помилка (частина Колпакова Михайла): {e}')
# Кінець частини Колпакова Михайла

# Початок частини Пося Назарія
try:
    # Читання json файлу
    with open(json_filename, 'r', encoding = 'utf-8') as json_file:
        json_data = json.load(json_file)
        
    # Додаємо нові дані
    json_data.append({"Ім'я": "Назарій", "Прізвище": "Пось", "Вік": 18, "День народження": "10.04.05"})
    
    # Запис у csv файл
    with open(csv_filename, 'w', newline = '', encoding = 'utf-8') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames = json_data[0].keys())
        csv_writer.writeheader()
        csv_writer.writerows(json_data)     

except Exception as e:
    print(f'Виникла помилка (частина Пося Назарія): {e}')
# Кінець частини Пося Назарія

# Початок частини Гордієнка Сергія
try:
    # Читання csv файлу
    with open(csv_filename, 'r', encoding = 'utf-8') as csv_file:
        csv_data = list(csv.DictReader(csv_file))

    # Додаємо нові дані
    csv_data.append({"Ім'я": "Сергій", "Прізвище": "Гордієнко", "Вік": 18, "День народження": "--.--.--"})

    # Запис у json файл
    with open(json_filename, 'w', encoding='utf-8') as json_file:
        json.dump(csv_data, json_file, ensure_ascii = False, indent = 2)

except Exception as e:
    print(f'Виникла помилка (частина Гордієнка Сергія): {e}')
# Кінець частини Гордієнка Сергія

# Початок частини Волошко Ганни
try:
    # Читання json файлу
    with open(json_filename, 'r', encoding = 'utf-8') as json_file:
        json_data = json.load(json_file)

    # Додаємо нові дані
    json_data.append({"Ім'я": "Ганна", "Прізвище": "Волошко", "Вік": 18, "День народження": "--.--.--"})

    # Запис у csv файл
    with open(csv_filename, 'w', newline = '', encoding = 'utf-8') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames = json_data[0].keys())
        csv_writer.writeheader()
        csv_writer.writerows(json_data)

except Exception as e:
    print(f'Виникла помилка (частина Волошко Ганни): {e}')
# Кінець частини Волошко Ганни

# Початок частини Зуєвої Євгенії
try:
    # Читання csv файлу
    with open(csv_filename, 'r', encoding = 'utf-8') as csv_file:
        csv_data = list(csv.DictReader(csv_file))

    # Додавання нових рядків
    csv_data.append({"Ім'я": "Євгенія", "Прізвище": "Зуєва", "Вік": 18, "День народження": "--.--.--"})

    # Запис у json файл
    with open(json_filename, 'w', encoding = 'utf-8') as json_file:
        json.dump(csv_data, json_file, ensure_ascii = False, indent = 2)

except Exception as e:
    print(f'Виникла помилка (частина Зуєвої Євгенії): {e}')
# Кінець частини Зуєвої Євгенії