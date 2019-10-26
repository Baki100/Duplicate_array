a = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
t = 2
ss = list()
if t not in a:
    ss.append([-1, -1])
for i, j in enumerate(a):
    if j == t:
        ss.append(i)
        ss = [min(ss), max(ss)]

print(ss)
# on my own simple solution
