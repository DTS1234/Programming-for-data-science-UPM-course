# I Write a program which will raise any number x to a positive
# power n using a “for loop“

def powerOfN(x:int, n:int):
    if(n == 0):
        print(f'{x} to the power of {n} is equal to 1')  
        return 1
    x_before = x
    for i in range(1, n):
        x*=x_before
    print(f'{x_before} to the power of {n} is equal to {x}')    
    return x

powerOfN(2, 5)
powerOfN(5, 3)
powerOfN(4, 0)
powerOfN(3, 3)

