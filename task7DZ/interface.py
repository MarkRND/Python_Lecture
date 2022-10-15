def choice():
    nam = int(input('Выберите режим. 1 - запись в книгу:  , 2 - поиск в книге по имени: '))
    return nam
def get_name_tel():
    mass = []
    last_name = input('Введите фамилию: ')
    mass.append(last_name)
    first_name = input('Введите имя: ')
    mass.append(first_name)
    phone_number = input('Введите номер телефона: ')
    mass.append(phone_number)
    return mass
    
def search_user():
    return input("Введите имя для поиска:  ")


