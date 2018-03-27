# -*- coding: utf-8 -*-

# функции для работы с файлом users.txt
def write(id, name):
    with open('users.txt', 'a') as f:
        f.write('%d;%s\n' % (id, name))

def fileToDict():
    d = []
    try:
        with open('users.txt') as f:
            for line in f:
                try:
                    key, val = line.split(';')
                    d.append(val)
                except:
                    pass
    except:
        print('File users.txt doesnt exists.')
    return d

def nextId():
    return len(fileToDict()) + 1
