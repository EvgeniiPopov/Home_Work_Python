#1- Вычислить число c заданной точностью d. Число Пи не просто обрезать с math.pi, а вычислить, используя формулы: Нилаканта, ряды Тейлора, серию Ньютона или серию Чудновских.

#Пример:

#- при d = 0.001, π = 3.141.    10^(-10)≤ d ≤10^-1

from math import factorial as fact
i = 1
sgn = -1
a = 13591409
b = 545140134
c = 640320
d = c ** (3/2)
s = a / d
ss = 3
while str(ss)[:12] != '3.1415926535' :
    tmp = (sgn * fact(6*i) * (a + b*i) /
    (fact(3*i) * fact(i) ** 3 * d * c**(3*i)))
    s += tmp
    sgn *= -1
    i += 1
    ss = 1 / (12*s)
print(ss)
print(i-1)

# 2- Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности. Посмотрели, что такое множество? Вот здесь его не используйте.

numbers = [20, 20, 30, 30, 40]

def get_unique_numbers(numbers):
    unique = []

    for number in numbers:
        if number in unique:
            continue
        else:
            unique.append(number)
    return unique

print(get_unique_numbers(numbers))


# 3- Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# Пример: при N = 12 -> [2, 3]

def Factor(n):
    Ans = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            Ans.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        Ans.append(n)
    return Ans
print(Factor(int(input("Введите число N: "))))
