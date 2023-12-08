#計算をする
def calculate(number1,number2,operand):
    num=0
    try:
        if operand=="+":
            num = str(number1 + number2)
        elif operand=='-' :
            num = str(number1 - number2)
        elif operand=='*':
            num = str(number1 * number2)
        elif operand=='/':
            num = str(number1 / number2)
    except ZeroDivisionError as e:
        num = e
    return num


