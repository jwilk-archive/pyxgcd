def xgcd(a, b):
    '''
    >>> xea(352, 168)
    [8, -10, 21]
    >>> xea(168, 352)
    [8, 21, -10]
    >>> xea(3458, 4864)
    [38, -45, 32]
    >>> xea(4181, 6765)
    [1, -2584, 1597]
    '''
    p, q = [a, 1, 0], [b, 0, 1]
    while q[0]:
        p, q = q, [x - p[0] // q[0] * y for x, y in zip(p, q)]
    return p

# vim:ts=4 sw=4 et
