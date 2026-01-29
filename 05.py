def LengthES(i):
    arr = [-999] + list(i)
    n = len(arr)

    L = [1] * n

    for p in range(n-1, -1, -1):
        max_length = 0
        for q in range(p+1, n):
            if arr[q] > arr[p]:
                max_length = max(max_length, L[q])

        L[p] = 1 + max_length

    return L[0]- 1
