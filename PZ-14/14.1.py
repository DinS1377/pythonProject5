# . В исходном текстовом файле(radio_stations.txt) найти все домены из URL-адресов
# (например, в URL-адресе http://stream.hoster.by:8081/pilotfm/audio/icecast.audio
# домен выделен полужирным)
import re

text = "http://stream.hoster.by:8081/pilotfm/audio/icecast.audio"
pattern = r'https?://([a-zA-Z0-9.-]+)'


with open ('radio_stations.txt', 'r', encoding='UTF-8') as file:
    for line in file:

        domain = re.search(pattern, line)
        if domain:
            print(domain.group(1))


# Упражнение по регуляркам
# Найдите все натуральные числа (возможно, окружённые буквами); \d+
# •	Найдите все «слова», написанные капсом (то есть строго заглавными), возможно внутри настоящих слов (аааБББввв); [А-ЯA-Z]+
# •	Найдите слова, в которых есть русская буква, а за ней цифра; \b[А-Яа-я]+\d[\d\w]+
# •	Найдите все слова, начинающиеся с русской или латинской большой буквы (\b — граница слова);\b[А-ЯA-Z]\w*
# •	Найдите слова, которые начинаются на гласную (\b — граница слова); \b[аеёиоуыэюяaeiou]\w+
# •	Найдите все натуральные числа, не находящиеся на границе слова; \b\d+\b
# •	Найдите строчки, в которых есть символ * (. — это точно не конец строки!); [^\n]*[*][^\n]*
# •	Найдите строчки, в которых есть открывающая и когда-нибудь потом закрывающая скобки;[^\n]*[(]*[)][^\n]*
# •	Выделите одним махом весь кусок оглавления (в конце примера, вместе с тегами); <a[\w\W]+
# •	Выделите одним махом только текстовую часть оглавления, без тегов; [<a ]([\w —']+)<
# •	Найдите пустые строчки; [\s]\n
# •	Найти все теги, не включая их содержимое. <[a/][\w\W]+?>