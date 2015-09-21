alpha = ("abcdefghijklmnopqrstuvwxyz")
for i in range(len(alpha)):
    for j in range(len(alpha)):
        if i != j:
            print(alpha[i] + alpha[j])
