from flask import Flask, render_template, request
import numpy as np
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        value1 = request.form['input_value'] # 入力された値を取得
        value2 = request.form['input_value'] # 入力された値を取得
        result = process_input(value1,value2) # 入力値を処理して結果を取得
        return render_template('result.html', result=result) # 結果を表示するページにリダイレクト

    return render_template('index.html') # 入力フォームを表示するページにリダイレクト


# 時間の範囲とステップサイズ
t_start = 0
t_end = 10
h = 0.01

# 初期値
x_0 = 1
y_0 = 0

# 方程式
def f(x, y):
    return -y, x

# イプシロンデルタ法
def epsilon_delta(x_n, y_n, h):
    f_n = f(x_n, y_n)
    x_n1 = x_n + h*f_n[0]
    y_n1 = y_n + h*f_n[1]
    f_n1 = f(x_n1, y_n1)
    x_n2 = x_n + h*(f_n[0] + f_n1[0])/2
    y_n2 = y_n + h*(f_n[1] + f_n1[1])/2
    return x_n2, y_n2

# シミュレーション
t = np.arange(t_start, t_end, h)
x = np.zeros_like(t)
y = np.zeros_like(t)
x[0] = x_0
y[0] = y_0
for i in range(len(t)-1):
    x[i+1], y[i+1] = epsilon_delta(x[i], y[i], h)

def process_input(x_input,y_input):
    # 入力値を処理して結果を返す関数
    return epsilon_delta(x_input,y_input,h)

if __name__ == '__main__':
    app.run()
