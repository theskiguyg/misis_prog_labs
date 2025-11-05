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

json_to_csv("src/data/lab05/samples/people.json", "src/data/lab05/out/people_from_json.csv")
csv_to_json("src/data/lab05/samples/people.csv", "src/data/lab05/out/people_from_csv.json")