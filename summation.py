n = int(input("Enter a number: "))

def sum(num):
    s = 0  
    i = 1  
    while i <= num:
        s += i  
        i += 1  
    return s

print(sum(n))
