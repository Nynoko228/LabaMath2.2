import matplotlib.pyplot as plt  # для графиков
# from pylab import mpl
import math
import numpy
from scipy.interpolate import CubicSpline, UnivariateSpline
from Form import Application
from scipy.signal import savgol_filter
# Аппроксимация полиномиальной кривой с одной переменной


import tkinter as tk  # для интерфейса


def formula():
    global x, y, fin
    a = x
    b = y
    a, b, fin = BuildSpline(a, b, len(y))
    root = tk.Toplevel()
    # print("fin", len(fin))
    app = Application(fin, master=root)
    app.mainloop()

# Функция tablegrid создаёт окно с таблицей для изменения координат точек
def tablegrid():
    root = tk.Tk()
    tk.Label(root,
             text="x").grid(row=0)
    tk.Label(root,
             text="y").grid(row=1)
    # Координаты по x
    x1 = tk.Entry(root)
    x2 = tk.Entry(root)
    x3 = tk.Entry(root)
    x4 = tk.Entry(root)
    x5 = tk.Entry(root)
    x6 = tk.Entry(root)
    x7 = tk.Entry(root)
    # Координаты по y
    y1 = tk.Entry(root)
    y2 = tk.Entry(root)
    y3 = tk.Entry(root)
    y4 = tk.Entry(root)
    y5 = tk.Entry(root)
    y6 = tk.Entry(root)
    y7 = tk.Entry(root)
    # Расположение ячеек для изменения значений
    x1.grid(row=0, column=1)
    x2.grid(row=0, column=2)
    x3.grid(row=0, column=3)
    x4.grid(row=0, column=4)
    x5.grid(row=0, column=5)
    x6.grid(row=0, column=6)
    x7.grid(row=0, column=7)
    y1.grid(row=1, column=1)
    y2.grid(row=1, column=2)
    y3.grid(row=1, column=3)
    y4.grid(row=1, column=4)
    y5.grid(row=1, column=5)
    y6.grid(row=1, column=6)
    y7.grid(row=1, column=7)
    # В lstX и lstY хранятся "ссылки" на ячейки таблицы
    lstX = [x1, x2, x3, x4, x5, x6, x7]
    lstY = [y1, y2, y3, y4, y5, y6, y7]
    # Кнопка для ввода новых значений в программу
    tk.Button(root,
              text='OK',
              command=root.quit).grid(row=3,
                                      column=4,
                                      sticky=tk.W,
                                      pady=4)
    global x, y
    # Заполняем ячейки таблицы базовыми значениями
    for i in range(len(lstX)):
        lstX[i].insert(0, x[i])
        lstY[i].insert(0, y[i])
    tk.mainloop() # Открываем окно с таблицей
    # Получаем значения из ячеек таблицы для дальнейшей работы программы
    X = [x1.get(), x2.get(), x3.get(), x4.get(), x5.get(), x6.get(), x7.get()]
    Y = [y1.get(), y2.get(), y3.get(), y4.get(), y5.get(), y6.get(), y7.get()]
    for i in range(len(X)):
        if X[i] != "":
            x[i] = float(X[i])
    for i in range(len(Y)):
        if Y[i] != "":
            y[i] = float(Y[i])
    grafik()
# Функция grafik вызывает функции BildSpline для вычисления значений и draw для построения графика
def grafik():
    global x, y, fin
    newX, newY, fin = BuildSpline(x, y, len(x)) # Получаем новые значения X и Y, а также функцию в TeX-коде
    draw(x, newY, y, newX)
    plt.legend(loc="upper left")
    plt.show()

# Приветственное окно с выбором действий
def HelloWidget(lstx, lsty):
    root1 = tk.Tk()
    root1.geometry("350x350")
    text = tk.Label(root1,
                    text="Вы хотите изменить данные?",
                    font=("Helvetica 11")).place(x=65, y=150)
    tk.Button(root1,
              text='Y',
              command=tablegrid,
              # command=root1.quit,
              font=("Helvetica 11")).place(x=95, y=180)
    tk.Button(root1,
              text='N',
              command=grafik,
              font=("Helvetica 11")).place(x=200, y=180)

    tk.Button(root1,
              text='Formula',
              command=formula,
              font=("Helvetica 11")).place(x=150, y=280)

    tk.mainloop()


# Вычисление сплайна
def BuildSpline(x, y, n):
    x = [float(x[i]) for i in range(len(x))]
    y = [float(y[j]) for j in range(len(y))]
    fin = []
    m = []
    Lambda = [0]
    Mu = [0]
    # Вычилим значения hi, hi+1, a, b, c, d, lambda и mu
    for i in range(1, n-1):
        hi = x[i] - x[i-1]
        hi1 = x[i+1] - x[i]
        Ci = hi/6
        Ai = (hi+hi1)/3
        Bi = hi1/6
        Di = ((y[i+1]-y[i])/hi1) - ((y[i]-y[i-1])/hi)
        # if (y[i]==0):
        #     print((-Bi)/(Ai+Ci*Lambda[i-1]), Mu[i-1])
        Lambda.append((-Bi)/(Ai+Ci*Lambda[i-1]))
        Mu.append((Di-Ci*Mu[i-1])/(Ai+Ci*Lambda[i-1]))
    m.append(Mu[-1])

    Lambda.append(0)
    Mu.append(0)
    # Вычисляем значения mi
    Y2 = [0 for i in range(n)]
    for i in range(5, 0, -1):
        Y2[i] = Lambda[i] * Y2[i+1] + Mu[i]
        Y2[i] = round(Y2[i], 2)
    pc = 6 # Количество точек в интервале
    X = [0 for i in range(pc*n+1)]
    Y = [0 for i in range(pc * n + 1)]
    X[0] = x[0]
    Y[0] = y[0]
    # Общая формула
    fin += [r"$S_{3}=y_{i-1}\frac{x_{i}-x}{h_{i}}+y_{i}\frac{x-x_{i-1}}{h_{i}}+\frac{(x_{i}-x)^{3}-h_{i}^{2}(x_{i}-x)}{6h_{i}}m_{i-1}+\frac{(x-x_{i-1})^{3}-h_{i}^{2}(x-x_{i-1})}{6h_{i}}m_{i}$"]
    for j in range(1, n):
        h = x[j] - x[j - 1]
        cnt = 0
        for i in range(pc+1):
            X[j*pc+i] = h/pc * i + x[j-1] # Добавление новых x, чтобы график выглядел лучше
            X[j*pc+i] = round(X[j*pc+i], 2)
            # Вычисление новых y по формуле
            Y[j*pc+i] = (x[j] - X[j * pc + i]) / h * y[j - 1] + (X[j * pc + i] - x[j - 1]) / h * y[j] + ((x[j] - X[j * pc + i]) * (x[j] - X[j * pc + i]) * (x[j] - X[j * pc + i]) - h * h * (x[j] - X[j * pc + i])) / 6 / h * Y2[j - 1] + ((X[j * pc + i] - x[j - 1]) * (X[j * pc + i] - x[j - 1]) * (X[j * pc + i] - x[j - 1]) - h * h * (X[j * pc + i] - x[j - 1])) / 6 / h * Y2[j]
            Y[j*pc+i] = round(Y[j*pc+i], 2)
            if ((X[j*pc+i]==x[j-1])):
                cnt += 1
                fin += [
                    rf"$S_{3}({X[j * pc + i]})={y[j - 1]}\frac{{({x[j]} - ({X[j * pc + i]}))}}{{{h}}} + ({y[j]})\frac{{({X[j * pc + i]} - ({x[j - 1]}))}}{{{h}}} + ({Y2[j - 1]})\frac{{({x[j]} - ({X[j * pc + i]}))^3 - ({h})^2  ({x[j]} - ({X[j * pc + i]}))}}{{(6*({h}))}} + ({Y2[j]})\frac{{({X[j * pc + i]} - ({x[j - 1]}))^3 - ({h})^2 ({X[j * pc + i]} - ({x[j - 1]}))}}{{6*({h})}}$"]
            if ((X[j*pc+i]==x[n-1])):
                cnt += 1
                fin += [
                    rf"$S_{3}({X[j * pc + i]})={y[j - 1]}\frac{{({x[j]} - ({X[j * pc + i]}))}}{{{h}}} + ({y[j]})\frac{{({X[j * pc + i]} - ({x[j - 1]}))}}{{{h}}} + ({Y2[j - 1]})\frac{{({x[j]} - ({X[j * pc + i]}))^3 - ({h})^2  ({x[j]} - ({X[j * pc + i]}))}}{{(6*({h}))}} + ({Y2[j]})\frac{{({X[j * pc + i]} - ({x[j - 1]}))^3 - ({h})^2 ({X[j * pc + i]} - ({x[j - 1]}))}}{{6*({h})}}$"]
    return X[pc:], Y[pc:], fin


# Функция draw рисует наши кривые на координатной плоскости
def draw(data_x, data_y_new, data_y_old, data_x_new):
    global x, y
    plt.scatter(x, y)
    plt.plot(x, y, label="Табличные данные")
    a, b, fin = BuildSpline(x, y, len(y))
    plt.plot(a, b, label="Интерполяция", color="black")


fin = []
x = [-2, -1, 0, 1, 2, 3, 4]
y = [4, 0, -1, 0, 5, 10, 12]
HelloWidget(x, y)
