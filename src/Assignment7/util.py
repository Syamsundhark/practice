def happiness(arr, A, B):
    happiness = 0
    for num in arr:
        if num in A:
            happiness += 1
        elif num in B:
            happiness -= 1
    return happiness