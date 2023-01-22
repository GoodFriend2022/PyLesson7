# from modul_menu import Menu
import function as f

# if __name__ == "__main__":
menu_items = [
    ("1", "Вывод автобусов"),
    ("2", "Запись автобусов"),
    ("3", "Вывод водителей"),
    ("4", "Запись водителей"),
    ("5", "Вывод маршрута"),
    ("6", "Запись маршрута"),
    ("7", "Удалить маршрут")
    ("8", "Выход")]

# menu = Menu(menu_items)
# menu.run('>: ')

for i in menu_items:
    print(' - '.join(i))
user_text = input('Введите номер меню: ')
if user_text == '1':
    f.show('buses.txt')
elif user_text == '2':
    f.add_to_file('buse.txt', f.bus)
elif user_text == '3':
    f.show('drivers.txt')
elif user_text == '4':
    f.add_to_file('drivers.txt', f.driver)
elif user_text == '5':
    print(f.convert_route())
elif user_text == '6':
    f.add_to_file('temp.txt', f.route, 'w')
    with open('way.txt', 'a', encoding='utf8') as datafile:
        datafile.write(', '.join(f.invers_route()[0]))



