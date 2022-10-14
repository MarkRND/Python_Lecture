import model
import logger


def get_expr():
    return input()

def show_res(a):
    print(a)


expression = get_expr()  #получение уровнение от пользователя
logger.log_expr(expression)
answer = model.evaluate_expr(expression)  #сохранения решения
logger.log_ans(answer)
show_res(answer) # вывод ответа