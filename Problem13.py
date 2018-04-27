import numpy as np
def read_file():
    with open("Problem11.txt") as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    return content

def largest_sum(grid):
    sum = 0
    print(len(grid))
    for row in grid:
        sum += int(row)
    str_sum = str(sum)
    print(str_sum[:10])
if __name__ == '__main__':
    grid = read_file()
    largest_sum(grid)
