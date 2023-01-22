# from modul_menu import Menu
import function as f
import os

# if __name__ == "__main__":
menu_items = [
    ("1", "Вывод автобусов"),
    ("2", "Запись автобусов"),
    ("3", "Вывод водителей"),
    ("4", "Запись водителей"),
    ("5", "Вывод маршрута"),
    ("6", "Запись маршрута"),
    ("7", "Поиск"),
    ("8", "Удаление"),
    ("9", "Выход")]

# menu = Menu(menu_items)
# menu.run('>: ')

os.system('cls')
while True:
    for i in menu_items:
        print(' - '.join(i))
    user_text = input('Введите номер меню: ')
    if user_text == '1':
        os.system('cls')
        f.show('buses.txt')
    elif user_text == '2':
        f.add_to_file('buses.txt', f.bus)
        os.system('cls')
    elif user_text == '3':
        os.system('cls')
        f.show('drivers.txt')
    elif user_text == '4':
        f.add_to_file('drivers.txt', f.driver)
        os.system('cls')
    elif user_text == '5':
        os.system('cls')
        print(f.convert_route())
    elif user_text == '6':
        f.add_to_file('temp.txt', f.route, 'w')
        route = f.invers_route()
        if type(route) == list:
            with open('way.txt', 'a', encoding='utf8') as datafile:
                datafile.write(', '.join(route[0]) + '\n')
        os.system('cls')
    elif user_text == '7':
        os.system('cls')
        while(True):
            for i in f.menu_find:
                print(' - '.join(i))
            user_find = input('Введите номер меню: ')
            if user_find == '1':
                os.system('cls')
                print(f.find_object('buses.txt', 'Введите номер автобуса: '))
            elif user_find == '2':
                os.system('cls')
                print(f.find_object('drivers.txt', 'Введите фамилию водителя: '))
            elif user_find == '3':
                os.system('cls')
                print(f.find_object('way.txt', 'Введите номер маршрута: '))
            elif user_find == '4':
                os.system('cls')
                break
            else: 
                os.system('cls')
                print('Введенный номер в меню отсутствует')
                break
    elif user_text == '8':
        os.system('cls')
        while(True):
            for i in f.menu_del:
                print(' - '.join(i))
            user_del = input('Введите номер меню: ')
            if user_del == '1':
                os.system('cls')
                print(f.del_object('buses.txt', 'Введите номер автобуса: '))
            elif user_del == '2':
                os.system('cls')
                print(f.del_object('drivers.txt', 'Введите фамилию водителя: '))
            elif user_del == '3':
                os.system('cls')
                print(f.del_object('way.txt', 'Введите номер маршрута: '))
            elif user_del == '4':
                os.system('cls')
                break
            else: 
                os.system('cls')
                print('Введенный номер в меню отсутствует')
                break
    elif user_text == '9':
        print('CHAO')
        break
    else: 
        print('Введенный номер в меню отсутствует')
        break



