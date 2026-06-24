x = int(input("enter a number : ")) 
if x > 0 :
    print("x is positive")
elif x < 0 : 
    print("x is negative")
else :
    print("x is zero")


total = 0
count = 0
maximum = 0
for i in range(5):
    x = int(input("Enter number: "))
    total = total + x
    count = count + 1
    if x > maximum or i == 0:
        maximum = x
avg = total/count
print("Total is: ", total)
print("Average is: ", avg)
print("Max is: ", maximum)