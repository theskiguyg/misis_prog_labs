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