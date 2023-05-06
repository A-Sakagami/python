#数学ライブラリ
import numpy as np
import scipy as sp
import sympy as sym

def Heff(M, H_app, H_K, alpha, Ms, A_ex, gamma):
    # M: 磁化の3次元ベクトル
    # H_app: 外部磁場の3次元ベクトル
    # H_K: 磁気異方性の3次元ベクトル
    # alpha: ギルバート減衰係数
    # Ms: 飽和磁化
    # A_ex: 交換エネルギーの強さ

    # スピン角運動量
    spin_ang_momentum = np.cross(M, H_app + H_K)

    # 交換エネルギーの勾配
    exchange_grad = 2 * A_ex / Ms ** 2 * np.gradient(M)

    # ギルバートダンピング
    gilbert_damping = alpha / (1 + alpha ** 2) * np.cross(spin_ang_momentum, M)

    # 式をまとめたもの
    return -gamma / (1 + alpha ** 2) * np.cross(spin_ang_momentum, M) - gamma * alpha / (1 + alpha ** 2) * np.cross(M, np.cross(spin_ang_momentum, M)) - exchange_grad - gilbert_damping

def LLGequation(gamma, alpha, ms, t):
    
    
    return 0



