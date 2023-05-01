import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# クォータニオンを生成する関数
def make_quaternion(angle, axis):
    q = np.array([np.cos(angle/2), np.sin(angle/2)*axis[0], np.sin(angle/2)*axis[1], np.sin(angle/2)*axis[2]])
    return q

# 四元数を回転行列に変換する関数
def quaternion_to_rotation_matrix(q):
    R = np.array([[1-2*q[2]**2-2*q[3]**2, 2*q[1]*q[2]-2*q[3]*q[0], 2*q[1]*q[3]+2*q[2]*q[0]],
                  [2*q[1]*q[2]+2*q[3]*q[0], 1-2*q[1]**2-2*q[3]**2, 2*q[2]*q[3]-2*q[1]*q[0]],
                  [2*q[1]*q[3]-2*q[2]*q[0], 2*q[2]*q[3]+2*q[1]*q[0], 1-2*q[1]**2-2*q[2]**2]])
    return R

# 回転軸と回転角度を指定する
axis = np.array([1,1,1]) / np.sqrt(3)  # 回転軸
angle = np.pi/4 # 回転角度

# クォータニオンを生成する
q = make_quaternion(angle, axis)

# クォータニオンを回転行列に変換する
R = quaternion_to_rotation_matrix(q)

# 四角形を定義する
# 座標を定義する
vertices = np.array([[1, 1, 1],
                     [-1, 1, 1],
                     [-1, -1, 1],
                     [1, -1, 1],
                     [1, 1, -1],
                     [-1, 1, -1],
                     [-1, -1, -1],
                     [1, -1, -1]])

# 線分を定義する
edges = [[0, 1], [1, 2], [2, 3], [3, 0], [4, 5], [5, 6], [6, 7], [7, 4], [0, 4], [1, 5], [2, 6], [3, 7]]

# 面を定義する
faces = [[0, 3, 2, 1], [4, 5, 6, 7], [1, 5, 4, 0], [2, 6, 5, 1], [3, 7, 6, 2], [0, 4, 7, 3]]

# 各面の色を定義する
colors = ["r", "b"]

# vertices を回転させる
rotated_vertices = vertices @ R

fig = plt.figure(figsize=(10, 5))

# 回転前の図形を描画する
ax = fig.add_subplot(121, projection='3d')
ax.set_box_aspect([1, 1, 1])
lines1 = Line3DCollection([vertices[edge] for edge in edges], colors='r')
ax.add_collection(lines1)
polygons1 = Poly3DCollection([vertices[face] for face in faces], facecolors="#ff5959", alpha=0.3)
ax.add_collection(polygons1)
ax.scatter(vertices[:, 0], vertices[:, 1], vertices[:, 2], c='red')

# 回転後の図形を描画する
rotated_lines = Line3DCollection([rotated_vertices[edge] for edge in edges], colors='b')
ax.add_collection(rotated_lines)
rotated_polygons = Poly3DCollection([rotated_vertices[face] for face in faces], facecolors="#6060ff", alpha=0.3)
ax.add_collection(rotated_polygons)
ax.scatter(rotated_vertices[:, 0], rotated_vertices[:, 1], rotated_vertices[:, 2], c='blue')

plt.show()

