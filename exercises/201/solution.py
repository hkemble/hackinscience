def is_alpha(word):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(len(word)):
        if word[i] not in alpha:
            return False
    return True
