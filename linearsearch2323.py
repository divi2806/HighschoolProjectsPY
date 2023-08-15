#linear search
lis1 = []
ele = int(input("Enter the number of elements"))
for i in range(ele):
    n = int(input("Enter the numbers"))
    lis1.append(n)
print(lis1)
elements = int(input("Enter the element u want to search"))
found = 0
for i in range(len(lis1)):
    if lis1[i]==elements:
        print("Element is present and found at index",i)
        found = 1
        break
    if found == 0:
        print("Element is not present in the list")