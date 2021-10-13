def addzeros(a):
    c = a.count(0)
    b = []
    for i in a:
        if i == 0:
            b.extend((0, 0))
        else:
            b.append(i)
    return b
print(addzeros([1,0,2,0,7,0]))