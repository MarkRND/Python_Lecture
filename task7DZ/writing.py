from interface import get_name_tel

mass = get_name_tel
def writing_csv():
    file = 'Phonebook.csv'
    with open (file, 'a', encoding = 'utf-8') as data:
        data.write(f'{mass[0]}; {mass[1]}; {mass[2]} \n')
def writing_txt(mass):
    file = 'Phonebook.txt'
    with open (file, 'a', encoding = 'utf-8') as data:
        data.write(f'{mass[0]} {mass[1]} || {mass[2]}\n\n')
        


