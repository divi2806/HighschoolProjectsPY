#prime and composite numbers in python
L = []
L2 = []
L3 = []
ele = int(input("Enter the number of elements"))
for i in range(ele):
    n = int(input("Enter the numbers"))
    L.append(n)
for i in L:
    for j in range(2,i):
        if i%j==0:
            L2.append(i)
            break
        else:
            continue
    else:
        L3.append(i)
print("Prime numbers are",L3)
print("Composite numbers are",L2)
          