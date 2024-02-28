import numpy as np
import tkinter as tk
from tkinter import ttk
import calc

forms = tk.Tk()
error_message = tk.StringVar()
#数字１
number1 = tk.StringVar()
#四則記号
operand = ["+","-","*","/"]
#フォームで選択した記号
selected_option = tk.StringVar(value=operand[0])
#数字２
number2 = tk.StringVar()

#フォーム内に数値のみを許すための関数
def validate_number(input):
    try:
        float(input)
        return True
    except ValueError:
        return False

forms.title("四則演算デモ")
forms.geometry("500x300")
frame = ttk.Frame(forms, borderwidth=32)
frame.grid()

area1 = ttk.Label(frame, padding=(5,2),text="数字1")
area1.grid(row=0,column=0,sticky=tk.W)
area1_num1 =ttk.Entry(
    frame,
    validate="key",
    validatecommand=(frame.register(validate_number),'%P'),
    invalidcommand=lambda:  (area1_num1.config({"background": "pink"}), error_message.set("数値を入力してください")),
    textvariable=number1,
    width=10
)
area1_num1.grid(row=0,column=1,sticky=(tk.W,tk.E))

area2 = ttk.Label(frame, padding=(5,2),text="計算符号")
area2.grid(row=1,column=0,sticky=tk.W)

       
area2_button1 = tk.Radiobutton(frame, text="足し算", variable=selected_option ,value=operand[0])
area2_button2 = tk.Radiobutton(frame, text="引き算", variable=selected_option, value=operand[1])
area2_button3 = tk.Radiobutton(frame, text="かけ算", variable=selected_option, value=operand[2])
area2_button4 = tk.Radiobutton(frame, text="わり算", variable=selected_option, value=operand[3])
area2_button1.grid(row=1,column=1,sticky=(tk.W,tk.E))
area2_button2.grid(row=1,column=2,sticky=(tk.W,tk.E))
area2_button3.grid(row=1,column=3,sticky=(tk.W,tk.E))
area2_button4.grid(row=1,column=4,sticky=(tk.W,tk.E))

area3 = ttk.Label(frame, padding=(5,2),text="数字2")
area3.grid(row=2,column=0,sticky=tk.W)
area3_num2 =ttk.Entry(
    frame,
    validate="key",
    validatecommand=(frame.register(validate_number),'%P'),
    invalidcommand=lambda:  (area3_num2.config({"background": "pink"}), error_message.set("数値を入力してください")),
    textvariable=number2,
    width=10
)
area3_num2.grid(row=2,column=1,sticky=(tk.W,tk.E))

#計算ボタンを押したときの挙動
def calculate_button_clicked():
    num1value = float(area1_num1.get())
    operandvalue = selected_option.get()
    num2value = float(area3_num2.get())
    result = calc.calculate(num1value,num2value,operandvalue)
    result_label.configure(text=result)

calculate_button = ttk.Button(frame, text="計算", command=calculate_button_clicked)
calculate_button.grid(row=3, column=0,sticky=tk.W)
result_label = ttk.Label(frame, text="", padding=(5,2))
result_label.grid(row=4, column=0,sticky=tk.W)

forms.mainloop()