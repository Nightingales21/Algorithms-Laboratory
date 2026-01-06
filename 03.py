def partition1 (a, low, high):
    pivot = a[high]
    i = low
    j = high - 1
    while (i<j):
        if (a[i] < pivot):
            i+=1
        else:
            a[i], a[j] = a[j], a[i]
            j-=1
      
    print(a)
    return j+1

def partition (a, low, high):
    pivot = a[high]
    i = low
    j = high - 1
    while (i<j):
        if (a[i] < pivot):
            i+=1
        else:
            a[i], a[j] = a[j], a[i]
            j-=1
    a[i], a[high] = a[high], a[i]        
    return a

