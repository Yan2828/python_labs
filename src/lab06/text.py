def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if text is None:
        raise ValueError
    if not isinstance(text, str):
        raise TypeError
    if len(text) == 0:
        return ""  
    if yo2e:
        text = text.replace('Ё', 'Е').replace('ё', 'е')
    if casefold:
        text = text.casefold()
    text = text.replace('\t', ' ')    # табуляция
    text = text.replace('\r', ' ')    # возврат каретки  
    text = text.replace('\n', ' ')    # новая строка
    while '  ' in text:
        text = text.replace('  ', ' ')
    text= text.strip()
    return text

# print(normalize("ПрИвЕт\nМИр\t"))  
# print(normalize("ёжик, Ёлка", yo2e=True))  
# print(normalize("Hello\r\nWorld"))  
# print(normalize("  двойные   пробелы  ")) 

import re
def tokenize(text: str) -> list[str]:
    return re.findall(r"\w+(?:-\w+)*", text)

# print(tokenize("привет мир"))
# print(tokenize("hello,world!!!"))
# print(tokenize("по-настоящему круто"))
# print(tokenize("2025 год"))
# print(tokenize("emoji 😀 не слово"))

def count_freq(tokens: list[str]) -> dict[str, int]:
    if not tokens:
        return {}
    freq_dict = {}
    for token in tokens:
        freq_dict[token] = freq_dict.get(token, 0) + 1
    return freq_dict

# print(count_freq(["a","b","a","c","b","a"]))
# print(count_freq(["bb","aa","bb","aa","cc"]))

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    element = list(freq.items())
    element.sort(key = lambda i: (-i[1],i[0]))
    return element

# print(top_n(count_freq(["a","b","a","c","b","a"])))
# print(top_n(count_freq(["bb","aa","bb","aa","cc"])))


if __name__ == '__main__':
    print(normalize("ПрИвЕт\nМИр\t"))  
    print(normalize("ёжик, Ёлка", yo2e=True))  
    print(normalize("Hello\r\nWorld"))  
    print(normalize("  двойные   пробелы  ")) 

    print(normalize("ПрИвЕт\nМИр\t"))  
    print(normalize("ёжик, Ёлка", yo2e=True))  
    print(normalize("Hello\r\nWorld"))  
    print(normalize("  двойные   пробелы  "))     

    print(tokenize("привет мир"))
    print(tokenize("hello,world!!!"))
    print(tokenize("по-настоящему круто"))
    print(tokenize("2025 год"))
    print(tokenize("emoji 😀 не слово"))

    print(count_freq(["a","b","a","c","b","a"]))
    print(count_freq(["bb","aa","bb","aa","cc"]))
        
    print(top_n(count_freq(["a","b","a","c","b","a"])))
    print(top_n(count_freq(["bb","aa","bb","aa","cc"])))