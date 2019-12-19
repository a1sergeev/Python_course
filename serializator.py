#
import pickle
import json

def serialize(my_text):
    answer = input('Choose pickle or json? : ').lower()
    if answer == 'pickle':
        with open('Z7file.pickle', 'ab') as f:
            pickle.dump(my_text, f)
        print('Записанно в Z7file.pickle')
    elif answer == 'json':
        with open('Z7file.json', 'a', encoding='utf-8') as f:
            json.dump(my_text, f)
        print('Записанно в Z7file.json')
    else:
        print('Непонял ', end=' ')
        serialize(my_text)

