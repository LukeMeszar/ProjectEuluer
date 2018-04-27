def parse_file():
    with open('p022_names.txt') as f:
        content = f.readlines()
    names = content
    print(len(names))
    print(names)
if __name__ == '__main__':
    parse_file()
