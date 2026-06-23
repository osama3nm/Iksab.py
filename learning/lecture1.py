


name = "osama ali nemrawi"
print(name[0])
print(name[1])
print(name[-1])

print(name[0:5])
print(name[6:13])
print(name[0:13:2])
print(name[-7:])
print(name[-1::-1])
print(name.split()) #بعمل list من النص بناء على الفراغات بين الكلمات 
x = name.split() 
print(x)
print(type(x))

y = " ".join(x)  # بعمل نص من list بناء على الغراغات بين الكلمات 
print(y)

fruits = ['banana','apple','arange','kiwi']
vagetables = ['tomato','potato','cucumber']
grocery = fruits 
grocery.extend(vagetables) # بضيف list الى list اخرى 
print(grocery)

z = input('enter name : ')    # method to get input from user 
print("hello" , z )

age = input('enter your age : ')
age = int(age)
year_of_birth = 2026 - age 
print('your age is : ' , year_of_birth)