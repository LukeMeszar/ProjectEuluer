import itertools
from collections import defaultdict
def compute_sum_divisors(n):
    divisors_list = []
    for i in reversed(range(1,n)):
        if n % i == 0:
            divisors_list.append(i)
    return sum(divisors_list)



def find_amicable_numbers():
    nums = [x for x in range(1,10**4+1)]
    amicable_numbers = []
    sum_divisors_dic = defaultdict(int)
    for i in range(1,10**4 + 1):
        sum_divisors_dic[i] = compute_sum_divisors(i)
    print("done with divisors")
    for a,b in itertools.combinations(nums,2):
        if a != b:
            sum_a = sum_divisors_dic[a]
            sum_b = sum_divisors_dic[b]
            if sum_a == b and a == sum_b:
                amicable_numbers.append(a)
                amicable_numbers.append(b)
    return amicable_numbers

def sum_amicable_numbers(amicable_numbers):
    return sum(amicable_numbers)

if __name__ == '__main__':
    amicable_numbers = find_amicable_numbers()
    print(amicable_numbers)
    print(sum_amicable_numbers(amicable_numbers))
