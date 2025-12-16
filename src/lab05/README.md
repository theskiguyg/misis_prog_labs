# ЛАБОРАТОРНАЯ РАБОТА №5

## Задание А -> `src/lab05/json_csv.py`

#### **Требования**:
 - Проверка ошибок: 
    - неверный тип файла, пустой JSON или CSV → `ValueError`.
    - осутствующий файл → `FileNotFoundError`
 - Не использовать внешние пакеты (только json, csv, pathlib).
 - Все пути относительные.
 - Кодировка — строго UTF-8.


```python
import json, csv
from pathlib import Path

def json_to_csv(json_path: str, csv_path: str) -> None:
    jp = Path(json_path)
    if jp.suffix != ".json":
        raise ValueError("Неверный тип файла")
    if not jp.exists():
        raise FileNotFoundError("Файл не найден")
    with open(json_path,"r", encoding="utf-8") as f:
        data = json.load(f)
    if len(data)==0:
        raise ValueError("Пустой JSON")
    headers = list(data[0])
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)

def csv_to_json(csv_path: str, json_path: str) -> None:
    cp = Path(csv_path)
    if cp.suffix != ".csv":
        raise ValueError("Неверный тип файла")
    if not cp.exists():
        raise FileNotFoundError("Файл не найден")
    with open(csv_path,"r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    if len(rows) == 0:
        raise ValueError("Пустой CSV")
    with open(json_path,"w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)
```

![Вывод A_json_csv](../../images/lab05/5.1_jsoncsv.png)


## Выполнение:

### Обрабатываемые файлы -> `src/data/lab05/samples`

#### Перевод `CSV -> JSON`:

Исходный `src/data/lab05/samples/people.csv`
![Входной people_csv](../../images/lab05/sample/people_csv.png)

Результат перевода в JSON -> `src/data/lab05/out/people_from_csv.json`:
![Результат перевода people_from_csv](../../images/lab05/out/people_from_csv_json.png)

#### Перевод `JSON -> CSV`:

Исходный `src/data/lab05/samples/people.json`
![Входной people_json](../../images/lab05/sample/people_json.png)

Результат перевода в CSV -> `src/data/lab05/out/people_from_json.csv`:
![Результат перевода people_from_json](../../images/lab05/out/people_from_json_csv.png)


## Задание В -> `src/lab05/csv_xlsx.py`

#### **Требования**:
 - Проверка ошибок: 
    - неверный тип файла, пустой JSON или CSV → `ValueError`.
    - осутствующий файл → `FileNotFoundError`
 - Не использовать внешние пакеты.
 - Все пути относительные.
 - Кодировка — строго UTF-8.
 - Результат — открываемый XLSX с корректной структурой таблицы.

 ```python
import csv
from pathlib import Path
from openpyxl import Workbook

def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    cp = Path(csv_path)
    if cp.suffix != ".csv":
        raise ValueError("Неверный тип файла")
    if not cp.exists():
        raise FileNotFoundError("Файл не найден")

    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)
    if len(rows)==0:
        raise ValueError("Пустой CSV")

    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"
    for row in rows:
        ws.append(row)

    wb.save(xlsx_path)

csv_to_xlsx("src/data/lab05/samples/cities.csv", "src/data/lab05/out/cities.xlsx")
```
![Код 5.2](../../images/lab05/new_5.2_csvxlsx.png)

## Выполнение:

#### Перевод `CSV -> XLSX`:

Исходный `src/data/lab05/samples/cities.xlsx`
![Входной cities_xlsx](../../images/lab05/sample/people_csv.png)

Результат перевода в XSLX -> `src/data/lab05/out/cities.xlsx`:
![Результат перевода people_from_csv](../../images/lab05/out/done_city_xlsx.png)