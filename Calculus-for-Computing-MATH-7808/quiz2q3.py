import math

def derivative(f, a, method='central', h=0.01):
    if method == 'central':
        return (f(a + h) - f(a - h)) / (2 * h)
    elif method == 'forward':
        return (f(a + h) - f(a)) / h
    elif method == 'backward':
        return (f(a) - f(a - h)) / h
    else:
        raise ValueError("Method must be 'central', 'forward', or 'backward'.")


def f(x):
    return math.exp(math.cos(math.sqrt(x) - math.sin(math.sqrt(x))))


def bruteForce(xL, xR, prec):
    x = xL
    df0 = 10
    df1 = 10
    while df0*df1 > 0:
        df0 = derivative(prec, x)
        x = x + prec(x)
        df1 = derivative(prec, x)
    return x - prec(x)/2

print(bruteForce(1, 1, f))