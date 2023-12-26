import numpy as np
import tkinter as tk
from tkinter import ttk
import calc

forms = tk.Tk()
error_message = tk.StringVar()

#フォーム内に数値のみを許すための関数
def validate_number(input):
    try:
        float(input)
        return True
    except ValueError:
        return False
    
#入力フォームにエラーメッセージを表示するための関数
def clear_error_message():
    error_message.set("")

#数字１
number1 = tk.StringVar()
#四則記号
operand = np.array(["+","-","*","/"])
#数字２
number2 = tk.StringVar()

forms.title("四則演算デモ")
forms.geometry("500x300")
frame = ttk.Frame(forms, borderwidth=32)
frame.grid()

area1 = ttk.Label(frame, padding=(5,2),text="数字1")
area1.grid(row=0,column=0)
area1_num1 =ttk.Entry(
    frame,
    validate="key",
    validatecommand=(frame.register(validate_number),'%P'),
    invalidcommand=lambda:  (area1_num1.config({"background": "pink"}), error_message.set("数値を入力してください")),
    textvariable=number1,
    width=20
)
area1_num1.grid(row=0,column=1)

area2 = ttk.Label(frame, padding=(5,2),text="計算符号")
area2.grid(row=1,column=0)
area2_operand =ttk.Combobox(forms, textvariable=operand,values=[vec[0] for vec in operand] )
area2_operand.set(operand[0])
area2_operand.bind("<<ComboboxSelected>>")
area2_operand.grid(row=1,column=1)

area3 = ttk.Label(frame, padding=(5,2),text="数字2")
area3.grid(row=2,column=0)
area3_num2 =ttk.Entry(
    frame,
    validate="key",
    validatecommand=(frame.register(validate_number),'%P'),
    invalidcommand=lambda:  (area3_num2.config({"background": "pink"}), error_message.set("数値を入力してください")),
    textvariable=number2,
    width=20
)
area3_num2.grid(row=2,column=1)

#計算ボタンを押したときの挙動
def calculate_button_clicked():
    num1value = float(area1_num1.get())
    operandvalue = area2_operand.get()
    num2value = float(area3_num2.get())
    result = calc.calculate(num1value,num2value,operandvalue)
    result_label.configure(text=result)

calculate_button = ttk.Button(frame, text="計算", command=calculate_button_clicked)
calculate_button.grid(row=3, column=0)
result_label = ttk.Label(frame, text="", padding=(5,2))
result_label.grid(row=4, column=0)

forms.mainloop()