
import json
import csv
from pathlib import Path


def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON-файл в CSV.
    Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.
    Кодировка UTF-8. Порядок колонок — как в первом объекте или алфавитный (указать в README).
    """
    # Проверка существования файла
    json_file = Path(json_path)
    if not json_file.exists():
        raise FileNotFoundError(f"JSON файл не найден: {json_path}")
    
    # Проверка расширения файла
    if json_file.suffix.lower() != '.json':
        raise ValueError(f"Неверный тип файла: ожидается .json, получен {json_file.suffix}")
    
    # Чтение JSON файла
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        raise ValueError(f"Ошибка декодирования JSON: {e}")
    
    # Проверка, что данные - список словарей
    if not isinstance(data, list):
        raise ValueError("JSON должен содержать список объектов")
    if len(data) == 0:
        raise ValueError("JSON-файл пуст")
    if not isinstance(data[0], dict):
        raise ValueError("Элементы списка должны быть словарями")
    
    # Собираем все уникальные ключи из всех объектов
    all_keys = set()
    for item in data:
        all_keys.update(item.keys())
    fieldnames = list(all_keys)
    
    # Запись в CSV
    try:
        with open(csv_path, 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for row in data:
                # Заполняем отсутствующие поля пустыми строками
                row_complete = {key: row.get(key, '') for key in fieldnames}
                writer.writerow(row_complete)
    except IOError as e:
        raise IOError(f"Ошибка формата {e}") 
        
json_to_csv('data/lab05/samples/people.json', 'data/lab05/out/people_from_json.csv')


def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Преобразует CSV в JSON (список словарей).
    Заголовок обязателен, значения сохраняются как строки.
    json.dump(..., ensure_ascii=False, indent=2)
    """
    # Проверка существования файла
    csv_file = Path(csv_path)
    if not csv_file.exists():
        raise FileNotFoundError(f"CSV файл не найден: {csv_path}")
    
    # Проверка расширения файла
    if csv_file.suffix.lower() != '.csv':
        raise ValueError(f"Неверный тип файла: ожидается .csv, получен {csv_file.suffix}")
    
    # Чтение CSV файла
    try:
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            
            # Проверка наличия заголовков
            if reader.fieldnames is None:
                raise ValueError("CSV файл не содержит заголовков")
            
            data = list(reader)
            
    except Exception as e:
        raise ValueError(f"Ошибка чтения CSV файла: {e}")
    
    # Проверка, что CSV не пустой
    if not data:
        raise ValueError("CSV файл пуст")
    
    # Запись JSON файла
    try:
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            
    except Exception as e:
        raise ValueError(f"Ошибка записи JSON файла: {e}")


# Примеры использования (для тестирования)
csv_to_json('data/lab05/samples/people.csv', 'data/lab05/out/people_from_csv.json')

    