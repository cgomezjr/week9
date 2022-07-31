def printAll(seq):
    global count
    count += 1
    if seq:
        print("This is the argument #", count)
        print(seq[0])
        printAll(seq[1:])
        
count = 0      
printAll([1, 2, 3, 4, 5, 6, 7, 8, 9])

