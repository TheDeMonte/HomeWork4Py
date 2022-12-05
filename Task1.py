# 1 - Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]

def Decomposition(N):
    answer = []
    a = 2
    while a * a <= N:
        if N % a == 0:
            answer.append(a)
            N //= a
        else:
            a += 1
    if N > 1:
        answer.append(N)
    return answer


print(Decomposition(int(input())))
