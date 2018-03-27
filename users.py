# -*- coding: utf-8 -*-

# функции для работы с файлом users.txt
def write(id, name):
    with open('users.txt', 'a') as f:
        f.write('%d %s' % (id, name))

def fileToDict():
    d = {}
    try:
        with open('users.txt') as f:
            for line in f:
                key, val = line.split()
                d[int(key)] = val
    except:
        pass
    return d

def nextId():
    return len(fileToDict()) + 1
