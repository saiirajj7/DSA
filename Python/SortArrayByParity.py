


def SortArrayByParity(a):
    count = 0
    x = len(a)
    for i in range(0,x):
        if a[i]%2 == 0:
            temp = a[i]
            a[i] = a[count]
            a[count] = temp
            count = count + 1
    return a
print(SortArrayByParity([3,1,2,4]))