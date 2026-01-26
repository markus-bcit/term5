import math
from time import perf_counter
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

def trisention(xL, xR, prec, f):
    
    while xR-xL > prec:
        x1 = xL + (xR - xL) / 3
        x2 = xL + 2 * (xR - xL) / 3
        df0 = derivative(f, xL)
        df1 = derivative(f, x1)
        df2 = derivative(f, x2)
        if df0*df1 <= 0:
            xR = x1
        elif df1*df2 <= 0:
            xL = xL
            xR = x2
        else:
            xL = x1
    return (xL+xR)/2

start_time = perf_counter()

print("Min: ", end='')
print(bruteForce(1, 50, 0.00001, f))
print("Max: ", end='')
print(bruteForce(6, 50, 0.00001, f))

end_time = perf_counter()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time:.5f} seconds")
start_time = perf_counter()

print("Min: ", end='')
print(trisention(1, 50, 0.00001, f))
print("Max: ", end='')
print(trisention(6, 50, 0.00001, f))

end_time = perf_counter()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time:.5f} seconds")
