# lecture 2 : if elif else statement & for loop & while loop 

x = int(input("enter a number : ")) 
if x > 0 :
    print("x is positive")
elif x < 0 : 
    print("x is negative")
else :
    print("x is zero")

for i in range(1,11) :
   print(i)
   if i == 5 :
      break
   elif i == 3 :
      continue
   else :
      print("i is not 3 or 5")



