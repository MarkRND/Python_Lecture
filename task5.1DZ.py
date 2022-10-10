# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота


from random import randint
from secrets import choice


def Player(player_number, candys):
    print(f'Игрок -> {player_number}')
    while True:
        hod = int(input("Введите количество конфет от 1 до 28 -> "))
        if 0 < hod and hod < 29:
            candys -= hod
            print(f'Игрок взял -> {hod}. Осталось {candys}\n')
            break
        else:
            print("Ошибка, введите число конфет от 1 до 28")
    return candys
quantity = int(input("Введите количество игроков(1 или 2) -> "))

def Bot(candys):
    take = candys % 29
    if take == 0:
        take = randint(1, 28)
    candys -= take    
    print(f'Бот взял -> {take}. Осталось {candys}\n')
    return candys
def Game(participant_coll = 1, candys = 2021):
    participant_1 = choice([True, False])
    while candys > 28:
        if participant_1:
            candys = Player(1, candys)
            participant_1 = not participant_1
        elif participant_coll == 2:
            candys = Player(2, candys)
            participant_1 = not participant_1
        else:
            candys = Bot(candys)
            participant_1 = not participant_1
    if participant_1:
        print("Победил игрок -> 1 ")
    elif participant_coll == 2:
        print("Победил игрок -> 2 ")
    else:
        print("Увы, победил Бот")

Game(quantity, 2021)

