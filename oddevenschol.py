#odd even numbers in a list
list1 = []
list2 = []
list3 = []
ele = int(input("Enter the number of elements"))
for i in range(ele):
    n = int(input("Enter the numbers"))
    list1.append(n)
for i in list1:
    if i%2==0:
        list2.append(i)
    else:
        list3.append(i)
print("The odd numbers are",list3)
print("The even numbers are",list2)