class User:
    
    Allusers = []
    def __init__(self, name, username, password, height, age, weight):
        self.name = name
        self.username = username
        self.password = password
        self.height = height 
        self.age = age
        self.weight = weight

    @staticmethod
    def Login():
        username = input("Enter your username - ")
        password = input("Enter your password - ")

    @staticmethod
    def Register():
        name = input("Enter your fistname - ")
        username = input("Enter your username - ")
        password = input("Enter your password - ")
        age = int(input("Enter your age - "))
        weight = float(input("Enter your weight (kg) - "))
        height = float(input("Enter your height (cm) - "))

        newUser = User(name, username, password, height, age, weight) 
        Allusers.append(newUser)
        print(newUser)