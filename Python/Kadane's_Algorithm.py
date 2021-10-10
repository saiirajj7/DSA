def maxSubArraySum(a, size):
    max_current = max_global = a[0]
    for i in range(0, size):
        max_current = max(a[i], max_current + a[i])
        if max_current > max_global:
            max_global = max_current
    return max_global
a = [1,-2,-3,4,-4,1,4,-5]
print("Maximum contiguous sum is", maxSubArraySum(a, len(a)))