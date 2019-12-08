'''
Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
Строки необходимо пронумеровать. Если слово длинное, выводить только первые 10 букв в слове.

'''
#Вариант 1
num, text = 1, input('Введите строку и нескольких слов: ').split()
for word in text:
    print(num, word[0:10]) if len(word) > 10 else print(num, word, end='\n'); num += 1

'''
#Вариант 2
for word in text:
    if len(word) > 10:
        print(num, word[0:10]); num+=1
    else:
        print(num, word, end='\n'); num+=1
'''