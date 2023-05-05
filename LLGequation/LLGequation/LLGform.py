#入力フォームライブラリ
import tkinter as tk
from tkinter import ttk
from LLGequation import LLGequation

#TKオブジェクトをとりあえず作る
input_form = tk.Tk()
#磁気回転比γ
gyromagnetic_ratio = tk.StringVar()
#ギルバート定数α
GilbertConst = tk.StringVar()
#飽和磁化Ms
Ms = tk.StringVar()

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

error_message = tk.StringVar()

#入力フォーム
input_form.geometry("320x240")
input_form.title("ランダウ=リフシッツ=ギルバート方程式")
frame = ttk.Frame(input_form, borderwidth=32)
frame.grid()

label1 = ttk.Label(frame, text="磁気回転比", padding=(5,2))
label1.grid(row=0,column=0)
label1_num=ttk.Entry(
    frame,
    validate="key",
    validatecommand=(frame.register(validate_number), '%P'),
    invalidcommand=lambda: (label1_num.config({"background": "pink"}), error_message.set("磁気回転比には数値を入力してください")),
    textvariable=gyromagnetic_ratio,
    width=20
)
label1_num.grid(row=0,column=1)

label2 = ttk.Label(frame, text="ギルバート定数α", padding=(5,2))
label2.grid(row=1,column=0)
label2_num=ttk.Entry(
    frame,
    validate="key",
    validatecommand=(frame.register(validate_number), '%P'),
    invalidcommand=lambda: (label1_num.config({"background": "pink"}), error_message.set("ギルバート定数αには数値を入力してください")),
    textvariable=GilbertConst,
    width=20
)
label2_num.grid(row=1,column=1)

label3 = ttk.Label(frame, text="飽和磁化Ms", padding=(5,2))
label3.grid(row=2,column=0)
label3_num=ttk.Entry(
    frame,
    validate="key",
    validatecommand=(frame.register(validate_number), '%P'),
    invalidcommand=lambda: (label1_num.config({"background": "pink"}), error_message.set("飽和磁化Msには数値を入力してください")),
    textvariable=Ms,
    width=20
)
label3_num.grid(row=2,column=1)

#計算ボタンを押したときの挙動
def calculate_button_clicked():
    gyromagnetic_ratio_value = float(gyromagnetic_ratio.get())
    GilbertConst_value = float(GilbertConst.get())
    Ms_value = float(Ms.get())
    result = LLGequation(gyromagnetic_ratio_value, GilbertConst_value, Ms_value)
    result_label.configure(text=result)

calculate_button = ttk.Button(frame, text="計算", command=calculate_button_clicked)
calculate_button.grid(row=3, column=0)
result_label = ttk.Label(frame, text="", padding=(5,2))
result_label.grid(row=4, column=0)

input_form.mainloop()