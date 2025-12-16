# ЛАБОРАТОРНАЯ РАБОТА №6
## Задание А -> `src/lab06/cli_text.py`
#### **Требования**:
 - `stats --input <txt> [--top 5]` — анализ частот слов в тексте (использовать функции из `lab03`);
 - `cat --input <path> [-n]` — вывод содержимого файла построчно (с нумерацией при `-n`).

#### Выполнение:
```python
import argparse
from pathlib import Path
from src.lib.text import count_freq, top_n, normalize, tokenize


def main():
    parser = argparse.ArgumentParser(description="CLI‑утилиты лабораторной №6")
    subparsers = parser.add_subparsers(dest="command")

    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True)
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True)
    stats_parser.add_argument("--top", type=int, default=5)

    args = parser.parse_args()

    filepath = Path(args.input)

    if not filepath.exists():
        raise FileNotFoundError(f"Файл {filepath} не найден")

    if args.command == "cat":

        with filepath.open("r", encoding="utf-8") as f:
            num = 1
            for line in f:
                line = line.rstrip("\n")
                if args.n:
                    print(f"{num}: {line}")
                    num += 1
                else:
                    print(line)

    elif args.command == "stats":

        content = [i for i in filepath.open("r", encoding="utf-8")]
        tokens = tokenize(text="".join(content))
        freq = count_freq(tokens=tokens)
        top = top_n(freq=freq, n=args.top)

        num = 1
        for q, w in top:
            print(f"{num}. {q} - {w}")
            num += 1


if __name__ == "__main__":
    main()
```

#### Результат:
1. Вывод содержимого файла построчно (с нумерацией при `-n`).
Команда:
`python3 -m src.lab06.cli_text cat --input src/data/lab05/samples/cities.csv -n`

![Output 6.A](../../images/lab06/Вывод%20задание%20А%20ЛР6.png)

2. Анализ частот слов в тексте. 
Команда:
`python3 -m src.lab06.cli_text stats --input src/lab03/input.txt --top 5`

![Output 6.A2](../../images/lab06/Вывод%20задание%20А2%20ЛР6.png)



## Задание В -> `src/lab06/cli_convert.py`
#### **Требования**:
  - `json2csv --in data/samples/people.json --out data/out/people.csv`  
  - `csv2json --in data/samples/people.csv --out data/out/people.json`  
  - `csv2xlsx --in data/samples/people.csv --out data/out/people.xlsx`  

#### Выполнение:
```python
import argparse

from src.lab05.csv_xlsx import csv_to_xlsx
from src.lab05.json_csv import csv_to_json, json_to_csv


def main():

    parser = argparse.ArgumentParser(description="CLI-утилиты лабораторной №6")
    subparsers = parser.add_subparsers(dest="command")

    # --- json2csv ---
    json2csv_parser = subparsers.add_parser(
        "json2csv", help="Конвертировать JSON в CSV"
    )
    json2csv_parser.add_argument(
        "--in", dest="input", required=True, help="Путь к JSON-файлу"
    )
    json2csv_parser.add_argument(
        "--out", dest="output", required=True, help="Путь для CSV-файла"
    )

    # --- csv2json ---
    csv2json_parser = subparsers.add_parser(
        "csv2json", help="Конвертировать CSV в JSON"
    )
    csv2json_parser.add_argument(
        "--in", dest="input", required=True, help="Путь к CSV-файлу"
    )
    csv2json_parser.add_argument(
        "--out", dest="output", required=True, help="Путь для JSON-файла"
    )

    # --- csv2xlsx ---
    csv2xlsx_parser = subparsers.add_parser(
        "csv2xlsx", help="Конвертировать CSV в XLSX"
    )
    csv2xlsx_parser.add_argument(
        "--in", dest="input", required=True, help="Путь к CSV-файлу"
    )
    csv2xlsx_parser.add_argument(
        "--out", dest="output", required=True, help="Путь для XLSX-файла"
    )

    args = parser.parse_args()

    if args.command == "json2csv":
        json_to_csv(
            json_path=args.input,
            csv_path=args.output,
        )

    elif args.command == "csv2json":
        csv_to_json(
            csv_path=args.input,
            json_path=args.output,
        )

    elif args.command == "csv2xlsx":
        csv_to_xlsx(
            csv_path=args.input,
            xlsx_path=args.output,
        )


if __name__ == "__main__":
    main()
```

#### Результат:
1. **Конвертация `JSON -> CSV`**

 Команда:
`python3 -m src.lab06.cli_convert json2csv --in src/data/lab05/samples/people.json --out src/data/lab05/out/people_from_json.csv`
 
 Исходная директория `src/data/lab05/samples/people.json`:
![people.json](../../images/lab06/people_json.png)
 
 Результат в `src/data/lab05/out/people_from_json.csv`:
![people_from_json.csv](../../images/lab06/people_from_json.png)

2. **Аналогично и для `csv2json` & `csv2xlsx`**:
 
 -`python3 -m src.lab06.cli_convert csv2json --in src/data/lab05/samples/people.csv --out src/data/lab05/out/people_from_csv.json`
 
 -`python3 -m src.lab06.cli_convert csv2xlsx --in src/data/lab05/samples/cities.csv --out src/data/lab05/out/cities.xlsx`
