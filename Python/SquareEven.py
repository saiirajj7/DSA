def squareEven(a):
    b = []
    for i in range(len(a)):
        if i % 2 == 0:
            x = a[i] * a[i]
            b.extend([x])
        else:
            b.append(a[i])
    return b
a = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())
    a.append(ele)
print(squareEven(a))