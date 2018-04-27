def sum_digits():
    a = list(str(2**1000))
    b = sum(int(x) for x in a)
    print(b)

if __name__ == '__main__':
    sum_digits()
