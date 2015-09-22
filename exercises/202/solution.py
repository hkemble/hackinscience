def starts_with(haystack, needle):
    if needle == haystack[:len(needle)]:
        return True
    else:
        return False
