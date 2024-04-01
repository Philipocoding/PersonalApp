class User:
    
    Allusers = []
    def constructor(name, username, password, height, age, weight):
        this.name = name
        this.username = username
        this.password = password
        this.height = height 
        this.age = age
        this.weight = weight

@staticmethod
def Login():
    username = input("Enter your username - ")
    password = input("Enter your password - ")

@staticmethod
def Register():
    name = input("Enter your fistname - ")
    username = input("Enter your username - ")
    password = input("Enter your password - ")
    age = input("Enter your age - ")
    weight = input("Enter your weight (kg) - ")
    height = input("Enter your height (cm) - ")

    newUser = User(name, username, password, height, age, weight) 
    Allusers.append(newUser)
    print(newUser)