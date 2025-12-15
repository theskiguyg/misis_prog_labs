from re import finditer


def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if not (isinstance(text, str)):
        return TypeError
    if casefold:
        text = text.casefold()
    if yo2e:
        text = text.replace("Ё", "Е").replace("ё", "е")
    text = text.replace("\t", " ").replace("\r", " ").replace("\n", " ")
    text = " ".join(text.split())
    return text.strip()


def tokenize(text: str) -> list[str]:
    if not (isinstance(text, str)):
        return TypeError
    pattern = r"\w+(?:-\w+)*"
    string = text
    tokens = finditer(pattern, string)
    return [i.group() for i in tokens]


def count_freq(tokens: list[str]) -> dict[str, int]:
    if not (isinstance(tokens, list)):
        return TypeError
    freq = {}
    for i in tokens:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return freq


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    return sorted(freq.items(), key=lambda x: (-x[1], x[0]))[:n]
