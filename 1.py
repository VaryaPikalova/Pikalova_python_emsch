print("enter two integers")
k, n = map(int, input().split())
if n == k:
    print("")
while n > 0 and n != k:
    print("среднее арифметическое=",(n + k) / 2)
    print("среднее гармоническое=",2 / (1 / n + 1 / k))
    if n > k:
        print("максимальный элемент=", n)
        print("второй максимальный элемент=", (n - 1))
    else:
        print("максимальный элемент=", k)
        print("второй максимальный элемент=", (k - 1))
    if n < k:
        print("минимальный элемент=", n)
        print("второй мнимальный элемент=", (n + 1))
    else:
        print("минимальный элемент=", k)
        print("второй минимальный элемент=", (k + 1))
    break