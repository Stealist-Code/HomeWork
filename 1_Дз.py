while True:
    a = input('Введите слово: ')
    a = a.lower()
    a = a.replace(' ','')
    if a[::-1] == a:
        print('True')
    else:
        print('False')