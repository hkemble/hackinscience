file = open('words.txt')
count = [0] * 26
alpha = 'abcdefghijklmnopqrstuvwxyz'
for i in range(26):
    for j in file.read():
        if alpha[i] == j.lower():
            count[i] = count[i] + 1
total = sum(count)

print('a:',  round(count[0] / total, 2))
print('b:',  round(count[1] / total, 2))
print('c:',  round(count[2] / total, 2))
print('d:',  round(count[3] / total, 2))
print('e:',  round(count[4] / total, 2))
print('f:',  round(count[5] / total, 2))
print('g:',  round(count[6] / total, 2))
print('h:',  round(count[7] / total, 2))
print('i:',  round(count[8] / total, 2))
print('j:',  round(count[9] / total, 2))
print('k:',  round(count[10] / total, 2))
print('l:',  round(count[11] / total, 2))
print('m:',  round(count[12] / total, 2))
print('n:',  round(count[13] / total, 2))
print('o:',  round(count[14] / total, 2))
print('p:',  round(count[15] / total, 2))
print('q:',  round(count[16] / total, 2))
print('r:',  round(count[17] / total, 2))
print('s:',  round(count[18] / total, 2))
print('t:',  round(count[19] / total, 2))
print('u:',  round(count[20] / total, 2))
print('v:',  round(count[21] / total, 2))
print('w:',  round(count[22] / total, 2))
print('x:',  round(count[23] / total, 2))
print('y:',  round(count[24] / total, 2))
print('z:',  round(count[25] / total, 2))
