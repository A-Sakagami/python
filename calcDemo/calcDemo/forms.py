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
operand = tk.StringVar()
#数字２
number2 = tk.StringVar()

forms.geometry("400x300")
forms.title("四則演算デモ")
frame = ttk.Frame(forms, borderwidth=32)
frame.grid()

area1 = ttk.Label(frame, padding=(5,2))
area1.grid(row=0,column=0)
area1_num1 =ttk.Entry(
    frame,
    validate="key",
    validatecommand=(frame.register(validate_number),'%P'),
    invalidcommand=lambda:  (area1_num1.config({"background": "pink"}), error_message.set("数値を入力してください")),
    textvariable=number1,
    width=20
)

area2 = ttk.Label(frame, padding=(5,2))
area2.grid(row=0,column=1)
area2_operand =ttk.Combobox()