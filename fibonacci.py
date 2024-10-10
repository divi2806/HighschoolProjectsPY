#Print fibonacci sequence upto a given limit.
# 0,1,1,2,3,5,8,13,21,34......

def fibonacci(limit):
    a, b = 0,1
    sequence = []  
    while a < limit:
        sequence.append(a)
        a, b = b, a + b
    return sequence

n = int(input("Enter the limit : "))
print(fibonacci(n))