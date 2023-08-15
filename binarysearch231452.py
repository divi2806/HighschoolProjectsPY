#Binary search
lst = []
ele = int(input("Enter the number of elements"))
for i in range(ele):
    n = int(input("Enter the numbers"))
    lst.append(n)
a = int(input("Enter the number to be searched"))
length = 0
for i in lst:
    length+=1
    found = 0
for i in range(0,length-1):
    if i==a:
        print("The position of item",lst.index(a)+1)
        found = 1
    else:
        print("The item is not present")