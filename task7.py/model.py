import sympy

def evaluate_expr(expr):
    x = sympy.Symbol('X')
    return str(sympy.solve(expr,x))