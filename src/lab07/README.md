# ЛАБОРАТОРНАЯ РАБОТА №7

## Задание А -> `tests/test_text.py`

Написать автотесты для всех публичных функций модуля `src/lib/text.py`:

- `normalize(text: str) -> str`
- `tokenize(text: str) -> list[str]`
- `count_freq(tokens: list[str]) -> dict[str, int]`
- `top_n(freq: dict[str, int], n: int) -> list[tuple[str, int]]`

**Требования:**

- покрыть как минимум:
  - базовые случаи (обычный текст),
  - граничные случаи (пустые строки, повторы, спецсимволы),
  - сценарий с одинаковой частотой слов (проверка сортировки по алфавиту при равных значениях);
- использовать `pytest`.

#### Выполнение: 

```python
import pytest
from src.lib.text import normalize, tokenize, count_freq, top_n


@pytest.mark.parametrize(
    "source, expected",
    [
        ("ПрИвЕт\nМИр\t", "привет мир"),
        ("ёжик, Ёлка", "ежик, елка"),
        ("Hello\r\nWorld", "hello world"),
        ("  двойные   пробелы  ", "двойные пробелы"),
        ("", ""),
    ],
)
def test_normalize_basic(source, expected):
    assert normalize(source) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("привет мир", ["привет", "мир"]),
        ("hello,world!!!", ["hello", "world"]),
        ("по-настоящему круто", ["по-настоящему", "круто"]),
        ("2025 год", ["2025", "год"]),
        ("emoji 😀 не слово", ["emoji", "не", "слово"]),
        ("", []),
    ],
)
def test_tokenize_basic(text, expected):
    assert tokenize(text) == expected


def test_count_freq_and_top_n():
    tokens = ["a", "b", "a", "c", "b", "a"]
    freq = count_freq(tokens)
    assert freq == {"a": 3, "b": 2, "c": 1}
    assert top_n(freq, 2) == [("a", 3), ("b", 2)]


def test_top_n_tie_breaker():
    tokens = ["bb", "aa", "bb", "aa", "cc"]
    freq = count_freq(tokens)
    assert top_n(freq, 2) == [("aa", 2), ("bb", 2)]


def test_count_freq_empty_tokens():
    assert count_freq([]) == {}


def test_top_n_empty_freq():
    assert top_n({}, 5) == []

```

## Задание В -> `tests/test_json_csv.py`

Тесты для `src/lab05/json_csv.py`

Написать автотесты для функций:

- `json_to_csv(src_path: str, dst_path: str)`
- `csv_to_json(src_path: str, dst_path: str)`

#### Выполнение: 

```python
import pytest
import csv
import json
from pathlib import Path
from src.lab05.json_csv import json_to_csv, csv_to_json


def test_json_to_csv_roundtrip(tmp_path: Path):
    src = tmp_path / "people.json"
    dst = tmp_path / "people.csv"
    data = [
        {"name": "Alice", "age": 22},
        {"name": "Bob", "age": 25},
    ]
    src.write_text(
        json.dumps(data, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    json_to_csv(str(src), str(dst))

    with dst.open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))

    assert len(rows) == len(data)
    assert {"name", "age"} <= set(rows[0].keys())


def test_csv_to_json_roundtrip(tmp_path: Path):
    src = tmp_path / "people.csv"
    dst = tmp_path / "people.json"
    rows = [
        {"name": "Alice", "age": "22"},
        {"name": "Bob", "age": "25"},
    ]
    with src.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "age"])
        writer.writeheader()
        writer.writerows(rows)

    csv_to_json(str(src), str(dst))
    data = json.loads(dst.read_text(encoding="utf-8"))

    assert len(data) == len(rows)
    assert set(data[0].keys()) == {"name", "age"}


def test_json_to_csv_raises_value_error(tmp_path: Path):
    src = tmp_path / "empty.json"
    dst = tmp_path / "out.csv"

    src.write_text("[]", encoding="utf-8")

    with pytest.raises(ValueError):
        json_to_csv(str(src), str(dst))


def test_csv_to_json_raises_value_error(tmp_path: Path):
    src = tmp_path / "empty.csv"
    dst = tmp_path / "out.json"

    src.write_text("", encoding="utf-8")

    with pytest.raises(ValueError):
        csv_to_json(str(src), str(dst))


def test_json_to_csv_raises_file_not_found_error():
    with pytest.raises(FileNotFoundError):
        json_to_csv("111.json", "out.csv")


def test_csv_to_json_raises_file_not_found_error():
    with pytest.raises(FileNotFoundError):
        csv_to_json("1111.csv", "out.json")
```


#### Результат:
 
 -`Тесты`
![Результат ЛР7](../../images/lab07/poetry_tests.png)

 -`Форматирование кода через poetry black`
 ![black](../../images/lab07/poetry_black.png)