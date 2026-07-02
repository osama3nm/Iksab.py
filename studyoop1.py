class student:
    user_name = 0
    def __init__(self,id,user,gba):    # constructor 
        self.__id = id
        self.__user = user 
        self.__gba = gba 
        student.user_name += 1
    def set_id(self,id):        # setter for id
        self.__id = id 

    def get_id(self):           # getter for id
        return self.__id 
    
    def set_user(self,user):    # setter for user
        self.__user = user 

    def get_user(self):         # getter for user
        return self.__user
    
    def set_gba(self,gba):      # setter for gba
        self.__gba = gba 

    def get_gba(self):         # getter for gba
        return self.__gba


student_1 = student(202420327,"ossmanm",9.9)
student_2 = student(202220304,"hamza",88.5)
student_3 = student(20232031,"noor",81.3)

print(student.user_name)
student_1.set_id(202420327)
print(student_1.get_id())
student_1.set_user("osama")
print(student_1.get_user())
student_1.set_gba(93.1)
print(student_1.get_gba())

