class User:
    def __init__(self,user_id,username):
         #constructor
         self.id=user_id
         self.name=username
         print("user created")
#pascal case is used for naming  classes in python which means to capitalize the first letter.
#we cannot leave the class or function empty after initialization we must write something in the body.
#or we will use the pass keyword to avoid getting an error.

user_1=User(3,"jhon") #object

print(user_1.id)
print(user_1.name)


#constructor : what should happen when we create an object of a class. it is a special method that is called when an object is created. it is used to initialize the attributes of the class.