#計算をする
def calculate(number1,number2,operand):
    num
    try:
        if operand=="足し算":
            num = str(number1 + number2)
        elif operand=='引き算' :
            num = str(number1 - number2)
        elif operand=='かけ算':
            num = str(number1 * number2)
        elif operand=='割り算':
            num = str(number1 / number2)
    except ZeroDivisionError as e:
        num = e
    return num


