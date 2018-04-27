from math import factorial
def sum_digits():
    a = list(str(factorial(100)))
    b = sum(int(x) for x in a)
    print(b)

if __name__ == '__main__':
    sum_digits()
