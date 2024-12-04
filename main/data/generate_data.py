import csv
import random

###### This Script Generates 300 lines of crime data in the crime_data.csv file ######

with open('crime_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    # Write header
    writer.writerow(['AreaID', 'Priority', 'ResourceRequirement'])
    
    # Write 300 lines of data
    for i in range(1, 301):
        area_id = i
        # Priority between 0-100, higher numbers for some areas to represent hotspots
        priority = random.randint(0, 100)
        # Resource requirement between 1-5 units
        resource_req = random.randint(1, 5)
        
        writer.writerow([area_id, priority, resource_req])

print("Generated crime_data.csv with 300 areas")