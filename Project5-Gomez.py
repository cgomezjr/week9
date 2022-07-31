def isSorted(lst, key=lambda x: x):
    for i, s in enumerate(lst[1:]):
        if key(s) < key(lst[i]):
            return False
    return True
