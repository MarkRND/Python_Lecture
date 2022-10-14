from asyncore import write


def log_expr(a):
    with open('task7.py\file7.txt', 'w') as f:
        f.write(f'Уравнение: {a} = 0 \n')

def log_ans(a):
    with open('task7.py\file7.txt', 'a') as f:
        f.write(f'Корни уравнения {a} \n')