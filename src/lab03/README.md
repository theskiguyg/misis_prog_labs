# ЛАБОРАТОРНАЯ РАБОТА №3


## Задание A -> `src/lib/text.py`
## Реализую функции в модуле `src/lib/text.py`. 
## Далее вывожу результат в `src/lab03/A.py`. 

### normalize

```python
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if not(isinstance(text, str)):
        return TypeError
    if casefold:
        text = text.casefold()
    if yo2e:
        text = text.replace('Ё', "Е").replace('ё', 'е')
    text = text.replace('\t', ' ').replace('\r', ' ').replace('\n', ' ')
    text = ' '.join(text.split())
    return text.strip()
```

### tokenize

```python
def tokenize(text: str) -> list[str]:
    if not(isinstance(text, str)):
        return TypeError
    pattern = r"\w+(?:-\w+)*"
    string = text
    tokens = finditer(pattern, string)
    return [i.group() for i in tokens]
```

### count_freq

```python
def count_freq(tokens: list[str]) -> dict[str, int]:
    if not(isinstance(tokens, list)):
        return TypeError
    freq = {}
    for i in tokens:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return freq
```

### top_n

```python
def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    return sorted(freq.items(), key=lambda x: (-x[1], x[0]))[:n]
```

### Вывод результата в `src/lab03/A.py`.
### Запуск из терминала `python3 -m src.lab03.A`. 

```python
from src.lib.text import normalize, tokenize, top_n, count_freq


print(normalize("ПрИвЕт\nМИр\t"))
print(normalize("ёжик, Ёлка", yo2e=True))
print(normalize("Hello\r\nWorld"))
print(normalize("  двойные   пробелы  "))


print(tokenize("привет мир"))
print(tokenize("hello,world!!!"))
print(tokenize("по-настоящему круто"))
print(tokenize("2025 год"))
print(tokenize("emoji 😀 не слово"))


print(top_n(count_freq(["a", "b", "a", "c", "b", "a"]), n=2))
print(top_n(count_freq(["bb", "aa", "bb", "aa", "cc"]), n=2))
```

![Вывод 3.А](../../images/lab03/A.png)

## Задание B -> `src/lab03/B_text_stats`

### Читаем текст из stdin `src/lab03/input.txt`, вызваем функции из `src/lib/text.py`, выводим статистику. 
### Запуск из терминала: `python3 -m src.lab03.B_text_stats < src/lab03/input.txt`. 

```python
import sys
from src.lib.text import count_freq, top_n, normalize, tokenize

text = sys.stdin.read()

tokens = tokenize(text=normalize(text=text))
top = top_n(count_freq(tokens))

print(f"Всего слов: {len(tokens)}")
print(f"Уникальных слов: {len(set(tokens))}")
print("Топ-5:")
for w, c in top:
    print(f"{w}:{c}")
```

![Вывод 3.B](../../images/lab03/B_text_stats.png)