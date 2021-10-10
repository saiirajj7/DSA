def Height_Checker(a):
    b = sorted(a)
    c = a
    x = len(a)
    count = 0
    for i in range (0,x):
        if b[i] != c[i]:
            count = count + 1
    return count
print(Height_Checker([3,2,1]))