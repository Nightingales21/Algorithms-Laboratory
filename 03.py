def partition1(a, low, high):
    pivot = a[high]
    i = low
    j = high

    while i < j:
        if a[i] < pivot:
            i += 1
        else:
            j -= 1
            a[i], a[j] = a[j], a[i]

    return i


def partition(a, low, high):
    pivot = a[high]
    i = low
    j = high

    while i < j:
        if a[i] < pivot:
            i += 1
        else:
            j -= 1
            a[i], a[j] = a[j], a[i]
    a[i], a[high] = a[high], a[i]
    return i

def qsort(a, low, high):
    if low > high:                     
        return a
    p = partition(a, low, high)     
    qsort(a, low, p - 1)
    qsort(a, p + 1, high)           
    return a