import csv
from Auser import User

def writeToFile(Allusers):
    with open('details.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        
        # Write headers (adjust as necessary)
        headers = ['name', 'username', 'password', 'height', 'age', 'weight']
        writer.writerow(headers)
        
        # Convert list of objects to list of lists
        rows = []
        for item in Allusers:
            row = [
                item.name,
                item.username,
                item.password,
                item.height,
                item.age,
                item.weight
            ]
            rows.append(row)
        
        # Write all rows at once
        writer.writerows(rows)

def ReadInFile():
    Userlist = []
    #str_User = ""
    tempUser = []
    user = User()
    with open('details.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')

        for row in spamreader:
           Userlist.append(row)


        User.Allusers.clear()
        
        for str_User in  Userlist:
            #str_User = Userlist[i]
            #item = file.readline().strip()
            tempUser.append(str(str_User).split(';'))
            #user.fistname = tempUser[0]
            #user.username = tempUser[1]
            #user.password = tempUser[2]
            #user.height = tempUser[3]
            #user.age = tempUser[4]
           # user.weight = tempUser[5]

            user(tempUser[0], tempUser[1], tempUser[2], tempUser[3], tempUser[4], tempUser[5])
            User.Allusers.Append(user)
        
        for i in range(6):
            print(user.Allusers[i].Firstname)
