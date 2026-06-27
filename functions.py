# Create Function 

def myhello(name = 'osama'):       # default value
    print(f"Hello {name}")

myhello("osama")                   # call function
myhello()                          # call function without argument to use default value


# Return values
def getsum(num1 , num2):
    total = num1 + num2
    return total 

print(getsum(10 ,20 ))
sum = getsum(10 , 20)
print(sum)

