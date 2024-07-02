import os

class User:
    Allusers = [] 

    def __init__(self):
        pass
    
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

        for i in range(len(User.Allusers)):
            if username == User.Allusers[i].username and password == User.Allusers[i].password:
               os.system('cls')
               print("Hello")
               break

            else:
                print("Nope")
                break
    @staticmethod
    def Register():
        from FileHandling import writeToFile
        from FileHandling import ReadInFile

        name = input("Enter your fistname - ")
        username = input("Enter your username - ")
        password = input("Enter your password - ")
        age = int(input("Enter your age - "))
        weight = float(input("Enter your weight (kg) - "))
        height = float(input("Enter your height (cm) - "))

        newUser = User(name, username, password, height, age, weight) 
        User.Allusers.append(newUser)
        writeToFile(User.Allusers)
        ReadInFile()