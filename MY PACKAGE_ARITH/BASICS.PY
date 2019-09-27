def sum(a,b):
    sum=a+b
    return sum
sum(2,4)

def swap(a,b):
    c=a
    a=b
    b=c
    return a,b
swap(22,45)

def fact(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact
fact(5)
def isprime(n):
    if n==2:
        return True
    for val in range(2,(n//2)+1):
        if n%val==0:
            return False
        else:
            return True      
for i in range(1,20):
    print("is prime",isprime(i))
        
