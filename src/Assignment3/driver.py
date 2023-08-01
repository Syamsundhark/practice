from src.Assignment3.util import *
n = int(input())
name, *line = input().split()
scores = list(map(float, line))
marks={}
marks[name] = scores
query_name = input()
avg(n,marks,name)