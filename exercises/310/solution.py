file = open('words.txt')
count = 0
for i in file.read():
    if i == 'e':
        count = count+1
print(count)
