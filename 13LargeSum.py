import csv

csv_list = []

with open('/home/owen/DemoPythonDS/LearnPython/ProjectEuler/resources/problem13.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    for row in csv_reader:
        csv_list.append(row)

sum = 0
        
for row in csv_list:
    if row[0].isdigit():
        sum += int(row[0])
            

# for row in csv_list:
#     if row.isdigit():
#         sum += int(row)
sum = str(sum)
print(sum[:10])