w = [13, 8, 6, 2, 25, 19, 20, 1]
li = []
#s = input("Please input s:")
def knap(w, s, n, l):
    global flag
    if s == 0:
        print(l)
        return True
    if s < 0:
        return False
    if s > 0 and n < 0:
        return False
    l.append(w[n])
    k = l
    if n == 7 and s == 19:
        print(l)
    #print("1", l)
    if knap(w, s - w[n], n - 1, k) == True:
        return True
    if n == 7 and s == 19:
        print("2", l)
    return knap(w, s, n - 1, l[:len(l) - 1])

print(knap(w, 19, len(w) - 1, li))