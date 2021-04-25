# Majority Element. A first Example. Infoarena.
# The naive approach.
def __elmaj(a):
    for x in a:
        if a.count(x) > len(a) // 2:
           return [x, a.count(x)]
    return -1

# Time Complexity O(n^2)
def elmaj(a):
    n = len(a)
    for i in range(0, n):
        count = 0
        for j in range(0, n):
            if a[j] == a[i]:
                count +=1
        if count > n // 2:
            return [a[i], count]
    return [-1,-1]

# Time Complexity O(n + k)
def _elmaj(a):
    n = len(a)
    arr = [0]*(n+1)
    for i in range(0, n):
        arr[a[i]] += 1
        pass
    for i in range(0, n):
        if arr[i] > n // 2:
           return [i,arr[i]]
    return [-1,-1]

# Divide et conquer.
# Linearithmic Time Complexity O(n log n).
def _elmaj_(a):
    pass

# Linear Time Complexity O(n)
def elmaj_Moore():
    pass

def main():
    a = [3, 4, 4, 3, 2, 3, 3]
    r = __elmaj(a)
    print(r[0],r[1])
main()
