def func() -> None:
    a = {'one': 1}
    b = {}
    for k, v in a.items():
        b[v] = k
    print(a,b)
    return
print(func())

