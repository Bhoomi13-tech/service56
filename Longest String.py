str1 = "This is my Book"
L = str1.split()
max = 0
c = ""
for I in L:
    if len(I) > max :
        c = I
        max = len(I)
print("Longest Word is",c)
