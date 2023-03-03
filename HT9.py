#1)Даны значения величины заработной платы заемщиков банка (zp) и значения их поведенческого кредитного скоринга (ks): 
zp = 35, 45, 190, 200, 40, 70, 54, 150, 120, 110, 
ks = 401, 574, 874, 919, 459, 739, 653, 902, 746, 832. 
#Используя математические операции, посчитать коэффициенты линейной регрессии, приняв за X заработную плату (то есть, zp - признак), а за y - значения скорингового балла (то есть, ks - целевая переменная). Произвести расчет как с использованием intercept, так и без.
import numpy as np
import matplotlib.pyplot as plt
x = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
y = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])

print(f'Расчет с использованием математических формул с intercept \nŷ = b0 + b1 ∗ x')
print()

n = len(x)

b1 = (np.mean(x*y) - np.mean(x) * np.mean(y)) / (np.mean(x**2) - np.mean(x)**2)
print(f'Коэффициент b1: {round(b1, 2)}')
b0 = np.mean(y) - b1*np.mean(x)
print(f'Коэффициент b0: {round(b0, 2)}')

y_pred = b0 + b1 * x
print(f'Уравнение линейной регрессии: ŷ = {round(b0, 2)} + {round(b1, 2)} * x')

print(f'Функция потерь: mse = {round(((y - y_pred)**2).sum() / n, 2)}')

plt.scatter(x, y, label = 'x, y')
plt.plot(x, y_pred, 'g', label = 'ŷ = 444.18 + 2.62 * x')
plt.xlabel('zp')
plt.ylabel('ks')
plt.legend()
x = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
y = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])
print(f'Расчет матричным методом без intercept \nŷ = b1 ∗ x')
print()

x1 = x.reshape((10, 1))
# print(x)
y1 = y.reshape((10, 1))
# print(y)

B = np.dot(np.linalg.inv(np.dot(x1.T,x1)), x1.T @ y1)
print(f'Коэффициент b1: {round(B[0,0], 2)}')

y_pred = B[0,0] * x
print(f'Уравнение линейной регрессии: ŷ = {round(B[0,0], 2)} * x')

print(f'Функция потерь: mse = {((y - y_pred)**2).sum() / n}')

plt.scatter(x1, y1, label = 'x, y')
plt.plot(x1, y_pred, 'r', label = 'ŷ = 5.89 * x')
plt.xlabel('zp')
plt.ylabel('ks')
plt.legend()

#####################################

#2)Посчитать коэффициент линейной регрессии при заработной плате (zp), используя градиентный спуск (без intercept).
# Функция потерь 𝑚𝑠𝑒 = (∑(𝑦 − 𝑦_𝑝𝑟𝑒𝑑)^2) / 𝑛
x = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
y = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])
print(f'Расчет методом градиентного спуска без intercept \nŷ = b1 ∗ x')
print()

def mse_(B1, y=y, x=x, n=10):
    return ((B1 * x - y)**2).sum() / n

alpha = 1e-6
b1 = 0.1
n=10

for i in range(1001):
    b1 -= alpha * (2/n) * np.sum((b1*x - y) * x)
    if i%100 == 0:
        print(f'Iteration = {i}, b1 = {b1}, mse = {mse_(b1)}')
print()

print(f'Функция потерь при b1 = {round(b1, 2)}: mse = {round(mse_(b1), 2)}')

print(f'Коэффициент b1: {round(b1, 2)}')

print(f'Уравнение линейной регрессии: ŷ = {round(b1, 2)} * x')

###################################

#3)Произвести вычисления как в пункте 2, но с вычислением intercept. Учесть, что изменение коэффициентов должно производиться на каждом шаге одновременно (то есть изменение одного коэффициента не должно влиять на изменение другого во время одной итерации).
x = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
y = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])

print(f'Расчет методом градиентного спуска с intercept \nŷ = b0 + b1 ∗ x')
print()

def mse_(B0, B1, y=y, x=x, n=10):
    return ((B0 + B1*x - y)**2).sum() / n

alpha = 1e-5
b0 = 1
b1 = 1
n=10

for i in range(3000000):
    b0 -= alpha * (2/n) * np.sum(b0 + b1*x - y)
    b1 -= alpha * (2/n) * np.sum((b0 + b1*x - y)*x)
    if i%500000 == 0:
        print(f'Iteration = {i}, b0 = {b0}, b1 = {b1}, mse = {mse_(b0, b1)}')
print()

y_pred = b0 + b1 * x
print(f'Уравнение линейной регрессии: ŷ = {round(b0, 2)} + {round(b1, 2)} * x')

print(f'Функция потерь: mse = {round(mse_(b0, b1), 2)}')

plt.scatter(x, y, label = 'x, y')
plt.plot(x, y_pred, 'g', label = 'ŷ = 444.18 + 2.62 * x')
plt.xlabel('zp')
plt.ylabel('ks')
plt.legend()
from sklearn.linear_model import LinearRegression

x = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
y = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])

x = x.reshape(-1, 1)

model = LinearRegression()
regres = model.fit(x, y)
b0 = regres.intercept_
b1 = regres.coef_[0]
y_pred = model.predict(x)
print(f'Уравнение линейной регрессии с intercept: ŷ = {round(b0, 2)} + {round(b1, 2)} * x')

model_1 = LinearRegression(fit_intercept=False)
regres = model_1.fit(x, y)
b1 = regres.coef_[0]
y_pred_1 = model_1.predict(x)
print(f'Уравнение линейной регрессии без intercept: ŷ = {round(b1, 2)} * x')

plt.scatter(x, y, label = 'x, y')
plt.plot(x, y_pred_0, 'g', label = 'ŷ = 444.18 + 2.62 * x')
plt.plot(x, y_pred_1, 'r', label = 'ŷ = 5.89 * x')
plt.xlabel('zp')
plt.ylabel('ks')
plt.legend()