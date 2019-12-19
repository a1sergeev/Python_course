'''
Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
'''
count = 0
f = open("z2.dat", "r", encoding='utf-8')
for line in f:
    str_split = line.split()
    str_len = len(str_split)
    print("{} -{} слов(а) ".format(line.replace('\n', ''), str_len))
    count += 1
f.close()
print(f'------- В файле {f.name}, {count} строк(а) -------')
