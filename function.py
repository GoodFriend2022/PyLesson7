

def read_data_from_file(filename):
    result = []
    with open(filename, 'r', encoding='utf8') as datafile:
        [result.append(i.strip('\n').split(', ')) for i in datafile]
        return result

def add_to_file(filename, data_list, do = 'a'):
    with open(filename, do, encoding='utf8') as datafile:
        datafile.write(data_list[0] + ', '.join([input(i) for i in data_list if i != data_list[0]]) + '\n')

show = lambda filename: print(read_data_from_file(filename))

def convert_route(file_way = 'way.txt', file_bus = 'buses.txt', file_driver = 'drivers.txt'):
    route = read_data_from_file(file_way)
    bus = read_data_from_file(file_bus)
    driver = read_data_from_file(file_driver)
    for i in route:
        for id in bus:
            if i[2].lower() == id[0].lower():
                i[2] = id[1]
        for id in driver:
            if i[3].lower() == id[0].lower():
                i[3] = id[1]
    return route

def invers_route(file_way = 'temp.txt', file_bus = 'buses.txt', file_driver = 'drivers.txt'):
    route = read_data_from_file(file_way)
    bus = read_data_from_file(file_bus)
    driver = read_data_from_file(file_driver)
    item_bus = route[0][2]
    item_driver = route[0][3]
    for id in bus:
        if route[0][2].lower() == id[1].lower():
            route[0][2] = id[0]
    if route[0][2] == item_bus:
        if input('Такой автобус до настоящего момента в автопарке отсутствовал. Добавить?' +
            '\nY/N >>> ').lower() == 'y':
            id_bus = int(bus[len(bus) - 1][0].strip('bus')) + 1
            with open(file_bus, 'a', encoding='utf8') as datafile:
                datafile.write(f'bus{id_bus}, {route[0][2]}\n')
            route[0][2] = f'bus{id_bus}'
        else: return False
    for id in driver:
        if route[0][3].lower() == id[1].lower():
            route[0][3] = id[0]
    if route[0][3] == item_driver:
        if input('Такой водитель в списке сотрудников отсутствует. Добавить?' +
            '\nY/N >>> ').lower() == 'y':
            id_driver = int(driver[len(driver) - 1][0].strip('driver')) + 1
            with open(file_driver, 'a', encoding='utf8') as datafile:
                datafile.write(f'driver{id_driver}, {route[0][3]}\n')
            route[0][2] = f'driver{id_driver}'
        else: return False   
    return route

def find_object(filename, ask):
    user_object = input(ask).lower()
    if filename == 'way.txt':
        objects = convert_route(filename)
    else: objects = read_data_from_file(filename)
    object = [i for i in objects if user_object == i[1].lower()]
    if object == []:
        return 'Искомого объекта не найдено'
    else: return object

def del_object(filename, ask):
    object = find_object(filename, ask)
    if type(object) != list:
        return object
    else:
        ask = input('Вы уверены? \n(Y/N) >>> ')
        if ask.lower() == 'y':
            objects = read_data_from_file(filename)
            new_objects = [i for i in objects if i[0] != object[0][0]]
            with open(filename, 'w', encoding='utf8') as datafile:
                for i in new_objects:
                    datafile.write(', '.join(i) + '\n')
        return f'{object} \t объект удален'

bus = ['bus', 'Введите id автобуса: ', 'А также гос. номер автобуса: ']
driver = ['driver', 'Введите id водителя: ', 'А также его фамилию: ']
route = ['m', 'Введите id маршрута: ', 'А также его номер: ', 'Введите гос номер автобуса: ', 'Введите фамилию водителя: ']
menu_find = [
    ("1", "Найти автобус"),
    ("2", "Найти водителя"),
    ("3", "Найти маршрут"),
    ("4", "Выход")]
menu_del = [
    ("1", "Удалить автобус"),
    ("2", "Удалить водителя"),
    ("3", "Удалить маршрут"),
    ("4", "Выход")]

