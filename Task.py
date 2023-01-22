import os

def Menu(text):
    if text == 'start':
        print('Введите порядковый номер требуемого действия: \n' + 
        '1 - Показать все записи \n' +
        '2 - Найти запись по вхождению частей имени \n' +
        '3 - Добавить новый контакт \n' +
        '4 - Удалить контакт \n' +
        '5 - Изменить номер телефона у контакта \n' +
        '6 - Выход') 
    elif text == 'person':
        print('Введите порядковый номер действия для найденного абонента: \n' + 
        '4 - Удалить контакт \n' +
        '5 - Изменить номер телефона у контакта \n' +
        '6 - Выход') 
    return int(input('>>> '))

def AddPerson(filename):
    with open(filename, 'a') as data:
        data.writelines('\n' + input('Введите фамилию > ') + ', ' + input('Введите имя > ') + ', ' +
        input('Введите отчество > ') + ', ' + input('Введите номер телефона > '))

def ReadFile(filename):
    person = []
    with open(filename, 'r+') as data:
        for line in data:
            person.append(line.split(', '))
    return person

def PrintFile(filename):
    os.system('cls')
    with open(filename, 'r+') as data:
        return print(data.read() + '\n')

def FindName(filename):
    os.system('cls')
    count = 0
    person = input('Введите часть имени или телефона абонента > ')
    while True:
        for item in ReadFile(filename):
            for i in item:
                if person in i.lower():
                    print(f'{item}\n')
                    result = item
                    count += 1
                    break
        if count > 1:
            person = input('Таких абонентов несколько, попробуйте ввести часть имени или телефона' +
            ' точнее\n >>> ')
            count = 0
        elif count < 1:
            person = input('Таких абонентов нет, попробуйте ввести часть имени или телефона еще раз >>> ')
        else: break
    return result
    
def DelPerson(filename):
    person = FindName(filename)
    ask = input('Удалить абонента? \n(Y/N) > ')
    if ask.lower() == 'y':
        with open(filename, 'r+') as data:
            for line in data:
                if list(line.split(', ')) != person:
                    with open('temp.txt', 'a') as data:
                        data.write(line)
        os.remove(filename)
        os.rename('temp.txt', filename)
    return

def CorrectTel(filename):
    person = FindName(filename)
    number = input('Введите номер телефона > ')
    ask = input('Изменить номер абонента? \n(Y/N) > ')
    if ask.lower() == 'y':
        with open(filename, 'r+') as data:
            for line in data:
                if list(line.split(', ')) != person:
                    with open('temp.txt', 'a') as data:
                        data.write(line)
        os.remove(filename)
        os.rename('temp.txt', filename)
        person[3] = number
        with open(filename, 'a') as data:
            data.write(', '.join(person) + '\n')
    return
    

          







