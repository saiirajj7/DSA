def maxi(a):
    y = 0
    x = max(a)
    count = 0
    for i in range(0,len(a)):
        while count < 3:
            if a[i] < x:
                y = a[i]
                count = count + 1
    return y
print(maxi([3,2,1]))