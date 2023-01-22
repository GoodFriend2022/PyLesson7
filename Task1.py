import Task as t
import os

os.system('cls')
file = 'direct.txt'


while True:
    number = t.Menu('start')
    if not number in range(1, 7):
        os.system('cls')
        print('Такого номера в меню не представлено. Перезапустите программу и попробуйте еще раз.\n')
        break
    elif number == 1:
        t.PrintFile(file)
    elif number == 2:
        t.FindName(file)
        number = t.Menu('person')
    elif number == 3:
        t.AddPerson(file)
    elif number == 4:
        t.DelPerson(file)
    elif number == 5:
        t.CorrectTel(file)
    else: break
        
    
    

    











