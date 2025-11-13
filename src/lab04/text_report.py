from io_txt_csv import read_text, write_csv
from text import normalize, tokenize, count_freq, top_n 
import sys

def main(input_path: str = "data/input.txt", output_path: str = "data/report.csv", encoding: str = "utf-8"):

    try:
        text = read_text(input_path, encoding=encoding)
    except FileNotFoundError:
        print(f"Файл не найден")
        sys.exit(1)
    except UnicodeDecodeError:
        print("Неправильная кодировка файла")
        sys.exit(1)
    '''
Означает принудительное завершение программы, передает системе
код завершения 1 ( 0 - успешное завершение, 1 или любое другое значение - завершилось с ошибкой)
'''
    tokens = tokenize(normalize(text))
    freq = count_freq(tokens)
    sorted_freq = top_n(freq)

    rows = sorted_freq
    header = ("word", "count")

    if output_path.suffix.lower() != '.csv':
        raise ValueError
    
    if rows:
        write_csv(rows, output_path, header=header)
    else:
        write_csv([], output_path, header=header)

    total_words = sum(freq.values())
    unique_words = len(freq)
    top_5 = sorted_freq[:5]

    print(f"Всего слов: {total_words}")
    print(f"Уникальных слов: {unique_words}")
    print("Топ-5 слов:")
    for word, count in top_5:
        print(f"{word}: {count}")

if __name__ == "main":
    main()