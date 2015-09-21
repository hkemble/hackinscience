alpha = ("abcdefghijklmnopqrstuvwxyz")
for i in range(len(alpha)):
    for j in range(i+1, len(alpha)):
        print(alpha[i] + alpha[j])
