#Binary search
arr = []
ele = int(input("Enter the elements"))
for i in range(ele):
    n = int(input("Enter the numbers"))
    arr.append(n)
print(arr)
x = int(input("Enter the element in speech"))
def search(arr, x):
  
    for i in range(len(arr)):
  
        if arr[i] == x:
            return i
        print("Found")
        
  
    return -1

    

        