from collections import defaultdict, OrderedDict
def longest_chain():
    sequence_length = defaultdict(int)
    for i in range(1,10**6+1):
        chain_length = collatz(i, sequence_length)
        sequence_length[i] = chain_length
        # print("\n\n\n")

    ordered_sequence_length = OrderedDict(sorted(sequence_length.items(), key=lambda t: -t[1]))
    print(list(ordered_sequence_length.items())[0])

def collatz(n, dic):
    chain_counter = 1
    while n != 1:
        if n in dic:
            # print("n in dic", n)
            chain_counter += dic[n] - 1
            return chain_counter
        elif n % 2 == 0:
            n = n/2
        else:
            n = 3*n + 1

        chain_counter += 1
        # print("chain_counter", chain_counter, "n", n)
    return chain_counter

if __name__ == '__main__':
    longest_chain()
