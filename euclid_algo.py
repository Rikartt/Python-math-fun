def euclidalgo(l):
    runeuclid = True
    while runeuclid:
        i = max(l)
        j = min(l)
        q = i-j
        l[l.index(i)] = q
        l = list(set(l))
        if len(l) <= 1:
            runeuclid = False
    return l

print(euclidalgo([int(x) for x in input("enter numbers separated by space: ").split(' ')]))