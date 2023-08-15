#rotating a list in python
L1 =[]
ele = int(input("Enter the elements"))
for i in range(ele):
    n = int(input("Enter the numbers"))
    L1.append(n)
print(L1)
n2 = int(input("Enter the elements you want to rotate"))
L1 = L1[-n2:]+L1[:-n2]
print(L1)
