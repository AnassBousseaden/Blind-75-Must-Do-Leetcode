def f(U_n, n):
    return 11+U_n - n*(16)


def suite(n: int, f, U_0) -> int:
    a = U_0
    for i in range(1, n+1):
        a = f(a, i-1)
    return a


print(suite(138746, f, -678))
