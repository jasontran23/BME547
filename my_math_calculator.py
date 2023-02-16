def sqrt(n):

    if type(n) is str:
        raise TypeError("Cannot send a string.")
    if n < 0:
        raise ValueError("You cannot send a negative number"
                         "to this function.")

    x = n
    y = 1

    e = 0.000001
    while (x - y > e):
        x = (x + y)/2
        y = n / x
    return x
