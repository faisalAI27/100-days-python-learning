class User:
    def __init__(self,user_id,username):
         #constructor
         self.id=user_id
         self.name=username
         self.followers=0
         self.following=0

    def follow(self,user):
         user.followers+=1
         self.following+=1

              
#pascal case is used for naming  classes in python which means to capitalize the first letter.
#we cannot leave the class or function empty after initialization we must write something in the body.
#or we will use the pass keyword to avoid getting an error.

user_1=User(1,"jhon") #object
user_2=User(2,"sam") #object
user_1.follow(user_2) #user_1 is following user_2

print(user_1.id)
print(user_1.name)
print("user 1 followers:",user_1.followers)
print("user 1 following:",user_1.following)
print("user 2 followers:",user_2.followers)
print("user 2 following:",user_2.following)

#constructor : what should happen when we create an object of a class. it is a special method that is called when an object is created. it is used to initialize the attributes of the class.