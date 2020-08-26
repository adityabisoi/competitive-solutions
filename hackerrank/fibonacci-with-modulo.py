def pisanoPeriod(m):
    previous, current = 0, 1
    for i in range(0, m * m):
        previous, current = current, (previous + current) % m

        # A Pisano Period starts with 01
        if (previous == 0 and current == 1):
            return i + 1


def fibo(n):
    arr = [None]*n
    arr[0], arr[1] = 1, 1
    for i in range(2, n):
        arr[i] = arr[i-1]+arr[i-2]
    return arr[n-1]


def get_fibonacci_huge_naive(n, m):
    x = fibo(n % pisanoPeriod(m))
    return x % m


print(get_fibonacci_huge_naive(239,1000))
