import matplotlib.pyplot as plt
import numpy


def BuildSpline(x, y, n):
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

    pc = 4
    X = [0 for i in range(pc*n+1)]
    Y = [0 for i in range(pc * n + 1)]
    xs = numpy.linspace(-2, 4, 18)
    X[0] = x[0]
    Y[0] = y[0]

    for j in range(1, n):
        h = x[j] - x[j - 1]
        for i in range(pc+1):
            X[j*pc+i] = h/pc * i + x[j-1]
            X[j*pc+i] = round(X[j*pc+i], 2)

            # Y[j*pc+i] = (y[j-1]*((x[i]-X[j*pc+i])/h)) + (y[j]*(X[j*pc+i]-x[j-1])/h) + ((Y2[j-1]*pow(((x[j])-X[j*pc+i]), 3) - pow(h, 2) * (x[j]-X[j*pc+i])) / 6*h) + ((Y2[j]*pow((X[j*pc+i]-(x[j-1])), 3) - pow(h, 2) * (X[j*pc+i]-(x[j-1]))) / 6*h)
            # Y[j*pc+i] = (y[j-1]*((x[i]-X[j*pc+i])/h)) + (y[j]*(X[j*pc+i]-x[j-1])/h) + ((Y2[j-1]*((x[j])-X[j*pc+i])*((x[j])-X[j*pc+i])*((x[j])-X[j*pc+i]) - h * h * (x[j]-X[j*pc+i])) / 6*h) + ((X[j*pc+i]-(x[j-1]))*(X[j*pc+i]-(x[j-1]))*(X[j*pc+i]-(x[j-1])) - h * h * (X[j*pc+i]-(x[j-1]))) / 6*h
            # Y[j*pc+i] = (x[j] - X[j * pc + i]) / h * y[j - 1] + (X[j * pc + i] - x[j - 1]) / h * y[j] + ((x[j] - X[j * pc + i]) * (x[j] - X[j * pc + i]) * (x[j] - X[j * pc + i]) - h * h * (x[j] - X[j * pc + i])) / 6 / h * Y2[j - 1] + ((X[j * pc + i] - x[j - 1]) * (X[j * pc + i] - x[j - 1]) * (X[j * pc + i] - x[j - 1]) - h * h * (X[j * pc + i] - x[j - 1])) / 6 / h * Y2[j]
            # Y[j*pc+i] = (x[j] - X[j * pc + i]) / h * y[j - 1] + (X[j * pc + i] - x[j - 1]) / h * y[j] + ((x[j] - X[j * pc + i]) * (x[j] - X[j * pc + i]) * (x[j] - X[j * pc + i]) - h * h * (x[j] - X[j * pc + i])) / 6 / h * Y2[j - 1] + ((X[j * pc + i] - x[j - 1]) * (X[j * pc + i] - x[j - 1]) * (X[j * pc + i] - x[j - 1]) - h * h * (X[j * pc + i] - x[j - 1])) / 6 / h * Y2[j]
            Y[j*pc+i] = (x[j] - X[j * pc + i]) / h * y[j - 1] + (X[j * pc + i] - x[j - 1]) / h * y[j] + ((x[j] - X[j * pc + i]) * (x[j] - X[j * pc + i]) * (x[j] - X[j * pc + i]) - h * h * (x[j] - X[j * pc + i])) / 6 / h * Y2[j - 1] + ((X[j * pc + i] - x[j - 1]) * (X[j * pc + i] - x[j - 1]) * (X[j * pc + i] - x[j - 1]) - h * h * (X[j * pc + i] - x[j - 1])) / 6 / h * Y2[j]
            # Y[j*pc+i] = round(Y[j*pc+i], 2)

    return X[pc:], Y[pc:]


x = [-2, -1, 0, 1, 2, 3, 4]
x = [float(x[i]) for i in range(len(x))]
y = [4, 0, -1, 0, 5, 10, 12]
y = [float(y[j]) for j in range(len(y))]
plt.scatter(x, y)
plt.plot(x, y, label="Табличные данные")
x, y = BuildSpline(x, y, len(y))

plt.plot(x, y, label="Интерполяция",  color="black")
plt.legend(loc="upper left")
plt.show()