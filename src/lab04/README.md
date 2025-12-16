# ЛАБОРАТОРНАЯ РАБОТА №4

## Задание А -> `src/lab04/io_txt_csv.py`

## Реализую функции: 
### 1. `read_text(path: str | Path, encoding: str = "utf-8") -> str`  
        - Открыть файл на чтение в указанной кодировке и вернуть содержимое **как одну строку**;  
        - Обрабатывать ошибки: если файл не найден — поднимать `FileNotFoundError` (пусть падает), если кодировка не подходит — поднимать `UnicodeDecodeError` (пусть падает);  
        - НО: в докстринге опишите, как пользователь может выбрать другую кодировку (пример: `encoding="cp1251"`).
### 2. `write_csv(rows: list[tuple | list], path: str | Path, header: tuple[str,...] | None) -> None`  
        - Создать/перезаписать CSV с разделителем `,`;  
        - Если передан `header`, записать его первой строкой;  
        - Проверить, что каждая строка в `rows` имеет одинаковую длину (иначе `ValueError`).

```python
import csv
from pathlib import Path
from typing import Iterable, Sequence


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    p = Path(path)
    return p.read_text(encoding=encoding)

def write_csv(rows: Iterable[Sequence], path: str | Path,
              header: tuple[str, ...] | None = None) -> None:
    p = Path(path)
    rows = list(rows)
    if rows:
        cols = len(rows[0])
        for r in rows:
            if len(r) != cols:
                raise ValueError("Разная длина строк")
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)
```

## Задание В -> `src/lab04/text_report.py`
### Запуск из терминала `python3 -m src.lab04.text_report`.

1) Читает **один** входной файл `data/input.txt`.  
2) Нормализует текст (`lib/text.py`), токенизирует и считает частоты слов.  
3) Сохраняет `data/report.csv` c колонками: **`word,count`**, отсортированными: count ↓, слово ↑ (при равенстве).  
4) В консоль печатает краткое резюме:  
   - `Всего слов: <N>`  
   - `Уникальных слов: <K>`  
   - `Топ-5:` (список из `top_n` из ЛР3)

```python
from src.lab04.io_txt_csv import read_text, write_csv
from src.lib.text import count_freq, top_n, normalize, tokenize
from pathlib import Path

def text_progress(text):
    tokens = tokenize(normalize(text))
    freq = count_freq(tokens)
    return tokens, freq

in_path = Path("src/data/lab04/input.txt")
out_path = Path("src/data/lab04/report.csv")

text = read_text(in_path)
tokens, freq = text_progress(text)
write_csv(top_n(freq, len(freq)), out_path, header=("word", "count"))

print("Всего слов:", len(tokens))
print("Уникальных слов:", len(freq))
print("Топ-5:")
for word, count in top_n(freq, 5):
    print(f"{word}: {count}")
```

## Выполнение:

### Вход -> `data/lab04/input.txt`:
Привет, мир!!! Привет!

### Вывод в терминале:
![Вывод задание 4](../../images/lab04/text_report.png)

### Отчет CSV -> `data/lab04/report.csv`:
![Вывод отчет CSV](../../images/lab04/report_csv.png)