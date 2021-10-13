def maxDiff(a,k):
    i, j = 0, 0
    b=[]
    l = len(a)
    for i in a:
        if i < k:
            x = i + k
            b.append(x)
        else :
            y = i - k
            b.append(y)
    for j in b:
        m = min(b)
        n = max(b)
        o = n - m
        return o
print(maxDiff([3, 9, 12, 16, 20],2))