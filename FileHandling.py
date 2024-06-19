import csv

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
