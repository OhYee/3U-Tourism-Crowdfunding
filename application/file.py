def readFromFile(filename):
    str = ''
    f = open(filename,'r',encoding='UTF-8')
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        str += line
    f.close()
    return str