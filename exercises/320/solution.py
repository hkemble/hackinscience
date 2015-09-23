file = open('words.txt')
A = file.read()
d = {}
total = 0
for j in A:
    try:
        d[j.lower()] = d[j.lower()] + 1
    except KeyError:
        d[j.lower()] = 1
del d["\n"]
del d["'"]
for i in d.keys():
    total = total + d[i]
for i in d.keys():
    print(i + ':', round(d[i]/total, 2))
