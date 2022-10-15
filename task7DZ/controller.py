import interface
from writing import writing_txt
from writing import writing_csv
import exp

def start():
    us_ch = interface.choice()
    if us_ch == 1:
        cont = interface.get_name_tel()
        # print(cont)
        writing_txt(cont)
        writing_csv(cont)
        
    elif us_ch == 2:
        cont = interface.search_user()
        exp.expr(cont)