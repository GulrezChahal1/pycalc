<<<<<<< HEAD
#functions to perform sum and subtraction
    values = expression.split(' ')
=======
def compute(expression):
    num0, operator, num1 = expression.split(' ')
    num0, num1 = int(num0), int(num1)
>>>>>>> use-unpacking
    num0 = int(values[0])
    operator = values[1]
    num1 = int(values[2])
    if operator == '+':
        return num0 + num1
    elif operator == '-':
        return num0 - num1
    else:
        print('unknown operator!')
        return none
