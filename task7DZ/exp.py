def expr(name):
    with open('Phonebook.txt', 'r', encoding='utf-8') as file:
        list = file.read().splitlines()
        for first_name in list:
            if name.casefold() in first_name.casefold():
                print(first_name)

