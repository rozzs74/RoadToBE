def tail(n, total=1):

    if n == 0:
        return  total
    print(f"n {n}")
    return tail(n - 1, n * total)
tail(500)