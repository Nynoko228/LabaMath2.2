import matplotlib.pyplot as plt  # для графиков
from pylab import mpl
import math
import numpy
from scipy.interpolate import CubicSpline, UnivariateSpline
from Form import Application
from scipy.signal import savgol_filter
# Аппроксимация полиномиальной кривой с одной переменной


import tkinter as tk  # для интерфейса


def formula():
    global x, y, fin
    x, y, fin = BuildSpline(x, y, len(y))
    fin += [r"$S_{3}=y_{i-1}\frac{x_{i}-x}{h_{i}}+y_{i}\frac{x-x_{i-1}}{h_{i}}+\frac{(x_{i}-x)^{3}-h_{i}^{2}(x_{i}-x)}{6h_{i}}m_{i-1}+\frac{(x-x_{i-1})^{3}-h_{i}^{2}(x-x_{i-1})}{6h_{i}}m_{i}$"]
    fin += [r"$S_{3}^{'}(x_{i}+0)=-\frac{h_{i+1}}{3}m_{i}-\frac{h_{i+1}}{6}m_{i+1}+\frac{y_{i+1}-y_{i}}{h_{i+1}}$"]
    fin += [r"$S_{3}^{'}(x_{i}-0)=\frac{h_{i}}{6}m_{i-1}-\frac{h_{i}}{3}m_{i}+\frac{y_{i}-y_{i-1}}{h_{i}}$"]
    root = tk.Toplevel()
    app = Application(fin, master=root)
    app.mainloop()


def mainWidget():
    root1 = tk.Tk()
    root1.geometry("350x350")
    text = tk.Label(root1,
                    text="Номер таблицы",
                    font=("Helvetica 11")).place(x=65, y=150)
    NumTbl = tk.Entry(root1).place(x=95, y=150)
    text1 = tk.Label(root1,
                     text="Значение интерполяции",
                     font=("Helvetica 11")).place(x=65, y=170)
    NumInt = tk.Entry(root1).place(x=95, y=170)
    tk.Button(root1,
              text='N',
              command=root1.quit,
              font=("Helvetica 11")).place(x=170, y=180)
    tk.Button(root1,
              text='Formula',
              command=formula,
              font=("Helvetica 11")).place(x=150, y=280)

    tk.mainloop()


def tkek():
    root = tk.Tk()
    tk.Label(root,
             text="x").grid(row=0)
    tk.Label(root,
             text="y").grid(row=1)

    x1 = tk.Entry(root)
    x2 = tk.Entry(root)
    x3 = tk.Entry(root)
    x4 = tk.Entry(root)
    x5 = tk.Entry(root)
    x6 = tk.Entry(root)
    x7 = tk.Entry(root)
    y1 = tk.Entry(root)
    y2 = tk.Entry(root)
    y3 = tk.Entry(root)
    y4 = tk.Entry(root)
    y5 = tk.Entry(root)
    y6 = tk.Entry(root)
    y7 = tk.Entry(root)

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
    lstX = [x1, x2, x3, x4, x5, x6, x7]
    lstY = [y1, y2, y3, y4, y5, y6, y7]
    tk.Button(root,
              text='OK',
              command=root.quit).grid(row=3,
                                      column=4,
                                      sticky=tk.W,
                                      pady=4)
    global x, y
    for i in range(len(lstX)):
        lstX[i].insert(0, x[i])
        lstY[i].insert(0, y[i])
    tk.mainloop()
    if (len(x) == 0) and (len(y) == 0):
        tk.Label(root,
                 text="interpolation").grid(row=2)
        interpoll = tk.Entry(root)
        interpoll.grid(row=2, column=1)
        X = [float(x1.get()), float(x2.get()), float(x3.get()), float(x4.get()), float(x5.get()), float(x6.get()),
             float(x7.get())]
        Y = [float(y1.get()), float(y2.get()), float(y3.get()), float(y4.get()), float(y5.get()), float(y6.get()),
             float(y7.get())]
        return X, Y
    else:
        X = [x1.get(), x2.get(), x3.get(), x4.get(), x5.get(), x6.get(),
             x7.get()]
        Y = [y1.get(), y2.get(), y3.get(), y4.get(), y5.get(), y6.get(),
             y7.get()]
        for i in range(len(X)):
            if X[i] != "":
                x[i] = float(X[i])
        for i in range(len(Y)):
            if Y[i] != "":
                y[i] = float(Y[i])
    grafik()


def grafik():
    global x, y
    newX, newY = BuildSpline(x, y, len(x))
    draw(x, newY, y, newX)
    mpl.rcParams['font.sans-serif'] = ['Arial']
    mpl.rcParams['axes.unicode_minus'] = False
    # plt.title(r"$y=a_{0}+a_{1}x+a_{2}x^{2}$")
    plt.legend(loc="upper left")
    plt.show()


def HelloWidget(lstx, lsty):
    root1 = tk.Tk()
    root1.geometry("350x350")
    text = tk.Label(root1,
                    text="Вы хотите изменить данные?",
                    font=("Helvetica 11")).place(x=65, y=150)
    tk.Button(root1,
              text='Y',
              command=tkek,
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
    for i in range(1, n-1):
        hi = x[i] - x[i-1]
        hi1 = x[i+1] - x[i]
        Ci = hi/6
        Ai = (hi+hi1)/3
        Bi = hi1/6
        Di = ((y[i+1]-y[i])/hi1) - ((y[i]-y[i-1])/hi)
        Lambda.append((-Bi)/(Ai+Ci*Lambda[i-1]))
        Mu.append((Di-Ci*Mu[i-1])/(Ai+Ci*Lambda[i-1]))
    m.append(Mu[-1])
    Lambda.append(0)
    Mu.append(0)

    # for i in range(6):
    #     m.append(Lambda[6-1-i]*m[i] + Mu[6-1-i])
    # print(m)
    #
    Y2 = [0 for i in range(n)]
    for i in range(5, 0, -1):
        Y2[i] = Lambda[i] * Y2[i+1] + Mu[i]
        Y2[i] = round(Y2[i], 2)

    pc = 6 # Количество точек в интервале
    X = [0 for i in range(pc*n+1)]
    Y = [0 for i in range(pc * n + 1)]
    X[0] = x[0]
    Y[0] = y[0]

    for j in range(1, n):
        h = x[j] - x[j - 1]
        for i in range(pc+1):
            X[j*pc+i] = h/pc * i + x[j-1]
            X[j*pc+i] = round(X[j*pc+i], 2)
            fin += [rf"$S_{3}({X[j*pc+i]})=({x[j]} - {X[j * pc + i]}) / {h} + ({X[j * pc + i]} - {x[j - 1]}) / {h} * {y[j]} + (({x[j]} - {X[j * pc + i]})^3) - {h}^2 * ({x[j]} - {X[j * pc + i]})) / 6{h} * {Y2[j - 1]} + (({X[j * pc + i]} - {x[j - 1]})^3) - {h}^2* ({X[j * pc + i]} - {x[j - 1]})) / 6{h} * {Y2[j]}$"]
            Y[j*pc+i] = (x[j] - X[j * pc + i]) / h * y[j - 1] + (X[j * pc + i] - x[j - 1]) / h * y[j] + ((x[j] - X[j * pc + i]) * (x[j] - X[j * pc + i]) * (x[j] - X[j * pc + i]) - h * h * (x[j] - X[j * pc + i])) / 6 / h * Y2[j - 1] + ((X[j * pc + i] - x[j - 1]) * (X[j * pc + i] - x[j - 1]) * (X[j * pc + i] - x[j - 1]) - h * h * (X[j * pc + i] - x[j - 1])) / 6 / h * Y2[j]
            Y[j*pc+i] = round(Y[j*pc+i], 2)

    return X[pc:], Y[pc:], fin


# Функция draw рисует наши кривые на координатной плоскости
def draw(data_x, data_y_new, data_y_old, data_x_new):
    global x, y
    # spl = CubicSpline(x, y)
    # spl = UnivariateSpline(x, y)
    # x1 = numpy.linspace(-2, 4, 30)
    # plt.plot(x1, data_y_new, label="подгоночная кривая", color="black")
    plt.scatter(x, y)
    plt.plot(x, y, label="Табличные данные")
    x, y, fin = BuildSpline(x, y, len(y))

    plt.plot(x, y, label="Интерполяция", color="black")

# print("Введите номер таблицы: ", end="")
# table = int(input())
table = 8
fin = []
match table:
    case 0:
        x = ""
        y = ""
        x, y = tkek()
    case 1:
        x = [-2, 0, 1, 3, 5, 6, 8]
        y = [5, -1, 2, 10, 24, 36, 38]
        HelloWidget(x, y)
    case 2:
        x = [0.5, 1, 1.5, 2, 2.5, 3, 3.5]
        y = [0.4, 0.3, 1, 1.7, 2.1, 3.4, 4]
        HelloWidget(x, y)
    case 3:
        x = [0.4, 0.8, 1.2, 1.6, 2, 2.4, 2.8]
        y = [0.43, 0.94, 1.91, 3.01, 4, 4.56, 5]
        HelloWidget(x, y)

    case 4:
        x = [4.5, 5.0, 5.5, 6.0, 6.5, 7, 7.5]
        y = [7.7, 9.4, 11.4, 13.6, 15.6, 17, 18]
        HelloWidget(x, y)
    case 5:
        x = [0, 0.5, 1, 1.5, 2, 2.5, 3]
        y = [25, 26, 4, 7, 6, 13, 20]
        HelloWidget(x, y)
    case 6:
        x = [1, 1.5, 2, 2.5, 3, 3.5, 4]
        y = [0.22, 23, 31, 43, 56, 82, 60]
        HelloWidget(x, y)
    case 7:
        x = [4.5, 5, 5.5, 6, 6.5, 7, 7.5]
        y = [7.7, 9.4, 11.4, 13.6, 15.6, 18.6, 20]
        HelloWidget(x, y)
    case 8:
        x = [-2, -1, 0, 1, 2, 3, 4]
        y = [4, 0, -1, 0, 5, 10, 12]
        HelloWidget(x, y)
    case 9:
        x = [0.1, 0.2, 0.4, 0.5, 0.6, 0.8, 1]
        y = [1, 2, 4, 7, 10, 16, 13]
        HelloWidget(x, y)

    case 10:
        x = [2, 4, 5, 7, 9, 10, 12]
        y = [0.4, 0.16, 2.5, 4.9, 9, 100, 120]
        HelloWidget(x, y)
