#Question 1
def ordered_insert(u, a):
    if len(a) == 0:
        return [u]
    if u <= a[0]:
        return [u] + a
    return [a[0]] + ordered_insert(u, a[1:])

#Question 2
def insertion_sort(a):
    if len(a) == 0:
        return []
    return ordered_insert(a[0], insertion_sort(a[1:]))

#Question 3
def ordered_merge(u,v):
    if len(u) == 0:
        return v
    else:
        return ordered_merge(u[1:], ordered_insert(u[0], v))

def ordered_merge_Iteration(u,v):
    if len(u) == 0:
        return v
    for element in u:
        v = ordered_insert(element, v)
    return v
        
#Question 4
def merge(u, v):
    if len(v) == 0:
        return u
    elif len(u) == 0:
        return v
    elif u[0] <= v[0]:
        return [u[0]] + merge(u[1:], v)
    elif u[0] > v[0]:
        return [v[0]] + merge(u, v[1:])
    
#Question 5
def merge_sort(u):
    if len(u) == 1:
        return u
    mid = len(u) // 2

    head = merge_sort(u[0:mid])
    tail = merge_sort(u[mid:])

    return ordered_merge(head, tail)
        

def main():
    u = [15,40,45]
    v = [5,10,20,35,50]
    w = ordered_merge_Iteration(u, v)
    print(w)
     
    u = [2, 3, 8, 9]
    v = [1, 4, 5, 7]
    w = merge(u, v)
    print(w)
    
    w = merge_sort([2, 8, 4, 9, 5, 6, 0])
    print(w)

main()



