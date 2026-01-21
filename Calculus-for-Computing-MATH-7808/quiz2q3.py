import math

# from https://patrickwalls.github.io/mathematicalpython/differentiation/differentiation/
def derivative(f, a, method='central', h=0.0001):
    if method == 'central':
        return (f(a + h) - f(a - h)) / (2 * h)
    elif method == 'forward':
        return (f(a + h) - f(a)) / h
    elif method == 'backward':
        return (f(a) - f(a - h)) / h
    else:
        raise ValueError("Method must be 'central', 'forward', or 'backward'.")


def f(x):
    return math.exp(math.cos(math.sqrt(x)) - math.sin(math.sqrt(x)))


def bruteForce(xL, xR, prec, f):
    x = xL
    df0 = 1
    df1 = 1

    while df0*df1 > 0:
        df0 = derivative(f, x)
        x = x + prec
        df1 = derivative(f, x)
    return x - prec/2

print("Min: ", end='')
print(bruteForce(1, 50, 0.0001, f))
print("Max: ", end='')
print(bruteForce(6, 50, 0.0001, f))

