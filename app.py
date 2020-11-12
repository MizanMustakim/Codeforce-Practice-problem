t = int(input(""))
M = []
def sum(t):
    i = 0
    while i < t:
        A, B = map(int, (input()).split())
        i += 1
        M.append([A, B])
    for i in range(len(M)):
        c = M[i][0] + M[i][1]
        print(c)

sum(t)