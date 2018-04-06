v = []
g = []
n = int(input('Wierzcholki: '))
for a in range(n):
    x = input('Wartosci: ').split()
    v.append(x)
    for a in v:
        print(a)

for i in range(n):
    c = 0
    for j in range(n):
        c+=int(v[i][j])
    g.append(c)
    print('Stopien wierzcholka numer',i+1,'wynosi:',g[i])
print('Stopien grafu:',max(g))
