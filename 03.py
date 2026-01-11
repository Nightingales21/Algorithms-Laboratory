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

def bruteforce(nuts, bolts):
    matches = {}

    for nut in nuts:
        for bolt in bolts:
            if nut == bolt:
                matches[nut] = bolt
                break

    return matches

def partition_modified(arr, low, high, pivot):
    i = low

    for j in range(low, high):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
        elif arr[j] == pivot:
            arr[j], arr[high] = arr[high], arr[j]

    arr[i], arr[high] = arr[high], arr[i]
    return i

def partition_nuts_and_bolts(nuts, bolts, low, high):
    pivot_index = partition_modified(nuts, low, high, bolts[high])
    partition_modified(bolts, low, high, nuts[pivot_index])
    return pivot_index

def match_nuts_bolts(nuts, bolts, low, high):
    if low >= high:
        return

    pivot_index = partition_nuts_and_bolts(nuts, bolts, low, high)
    match_nuts_bolts(nuts, bolts, low, pivot_index - 1)
    match_nuts_bolts(nuts, bolts, pivot_index + 1, high)

