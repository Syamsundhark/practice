from src.Assignment7.util import *

n, m = map(int, input().split())
arr = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

res = happiness(arr, A, B)
print(res)