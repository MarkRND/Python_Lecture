# Создайте программу для игры в ""Крестики-нолики"".

mass = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
for i in mass:
    print(i)

def CrossZero(mass):
    player_1 = True
    victory = False
    for number in range(9):
        if player_1:
            print("Первый игрок -> X")
        else:
            print("Второй игрок -> О")
        hod = input("Введите номер-> ")
        for i in range(len(mass)):
            for j in range(len(mass[i])):
                if mass[i][j] == hod:
                    if player_1:
                        mass[i][j] = "X"
                    else:
                        mass[i][j] = "O"
        for i in mass:
            print(i)
        if number > 2:
            victory = Check(mass)
            if victory:
                if player_1:
                    print("Первый игрок победил")
                    break
                else:
                    print("Второй игрок победил")
                    break
        player_1 = not player_1
    if not victory:
        print("Ничья")
def Check(mass):
    victory = False
    if mass[0][0] == mass[0][1] == mass[0][2]:
        victory = True
    elif mass[1][0] == mass[1][1] == mass[1][2]:
        victory = True
    elif mass[2][0] == mass[2][1] == mass[2][2]:
        victory = True
    elif mass[0][0] == mass[1][0] == mass[2][0]:
        victory = True
    elif mass[0][1] == mass[1][1] == mass[2][1]:
        victory = True
    elif mass[0][2] == mass[1][2] == mass[2][2]:
        victory = True
    elif mass[0][0] == mass[1][1] == mass[2][2]:
        victory = True
    elif mass[2][0] == mass[1][1] == mass[0][2]:
        victory = True
    return victory
CrossZero(mass)
