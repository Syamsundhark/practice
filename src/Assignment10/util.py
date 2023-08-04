import itertools

def prob(n, l, k):
    total_combinations = 0
    a_combinations = 0

    for combination in itertools.combinations(range(n), k):
        total_combinations += 1
        if any(l[i] == 'a' for i in combination):
            a_combinations += 1

    return round(a_combinations / total_combinations,4)