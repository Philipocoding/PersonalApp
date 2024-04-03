import csv

def writeToFile(Allusers):
    with open('details.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        for item in Allusers:
            intdata = f"{str(item.height)}{str(item.age)}{str(item.weight)}"
            row = f"{item.name}{item.username}{item.password}{intdata}"
           # row = f"{item.name},{item.username},{item.password},{item.height},{item.age},{item.weight}"
            print(row)
            writer.writerow(row)