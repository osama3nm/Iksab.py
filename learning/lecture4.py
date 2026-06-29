l =[]

while True :
    x = input("Enter a num or type q to exit")
    if x.lower() == "q":
        break
    x = float(x)
    l.append(x)
print(l)    

def average(li) :
    sum = 0
    for i in li :
        sum += i
    avg = sum/len(li)

    return avg

print(average(l))    

# part 2

def average1(*li):
    sum = 0 
    for i in li :
        sum += i
    avg = sum    /len(li)
    return avg 
print(average1(1,2,3,4,5))

# part 3 (factorial)
x = 5
z = 1
for i in range(x,0,-1):
    z = z*i
print(z)