def xgcd(a, b):
    '''
    >>> xgcd(352, 168)
    (8, -10, 21)
    >>> xgcd(168, 352)
    (8, 21, -10)
    >>> xgcd(3458, 4864)
    (38, -45, 32)
    >>> xgcd(4181, 6765)
    (1, -2584, 1597)
    '''
    p, q = (a, 1, 0), (b, 0, 1)
    while q[0]:
        p, q = q, [x - p[0] // q[0] * y for x, y in zip(p, q)]
    return tuple(p)

# vim:ts=4 sw=4 et
