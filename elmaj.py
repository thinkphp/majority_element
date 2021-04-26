# Majority Element. A first Example. Infoarena.
# Warmup Algorithms
# The naive approach.
# Brute Force O(n^2)
def __elmaj(a):
    for x in a:
        if a.count(x) > len(a) // 2:
           return [x, a.count(x)]
    return -1

# Time Complexity O(n^2)
# Brute Force
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
def elmaj_n_log_n(a):
    if len(a) == 0:
       return None
    if len(a) == 1:
        return a[0]
    half = len(a) // 2

    left = elmaj_n_log_n(a[0:half])
    right = elmaj_n_log_n(a[half:])

    if left == right:
        return left
    if a.count(left) > half:
        return left
    if a.count(right) > half:
        return right
    return None

# Linear Time Complexity O(n)
def elmaj_Moore(a):
    k = 0
    candidate = -1
    for x in a:
        if k == 0:
           candidate = x
           k = 1
        else:
            if x == candidate:
                k += 1
            else:
                k -= 1

    return candidate

def main():
    a = [3, 4, 4, 3, 2, 3, 3]
    #r = __elmaj(a)
    #print(r[0],r[1])
    print(elmaj_n_log_n(a))

main()
