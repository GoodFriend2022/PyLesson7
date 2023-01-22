

def read_data_from_file(filename):
    result = []
    with open(filename, 'r', encoding='utf8') as datafile:
        [result.append(i.strip('\n').split(', ')) for i in datafile]
        return result

def add_to_file(filename, data_list, do = 'a'):
    with open(filename, do, encoding='utf8') as datafile:
        datafile.write(data_list[0] + ', '.join([input(i) for i in data_list if i != data_list[0]]))

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
    for i in route:
        for id in bus:
            if i[2].lower() == id[1].lower():
                i[2] = id[0]
        for id in driver:
            if i[3].lower() == id[1].lower():
                i[3] = id[0]
    return route

def find_route(filename)

def del_route(filename):
    



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

bus = ['bus', 'Введите id автобуса: ', 'А также гос. номер автобуса: ']
driver = ['driver', 'Введите id водителя: ', 'А также его фамилию: ']
route = ['m', 'Введите id маршрута: ', 'А также его номер: ', 'Введите гос номер автобуса: ', 'Введите фамилию водителя: ']