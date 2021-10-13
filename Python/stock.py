def stock(a):
    maxProfit = 0
    minSoFar = a[0]
    for i in range(0, len(a)):
        minSoFar = min(a[i],minSoFar)
        profit = a[i] - minSoFar
        maxProfit = max(profit, maxProfit)
    return maxProfit
print(stock([7,1,5,3,6,4]))
