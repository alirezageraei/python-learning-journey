import csv

def save_data(data):
    
    with open("tasks.csv", "w",newline="") as t:
        
        Headings = ["name", "description", "priority"]
        writer = csv.DictWriter(t, fieldnames=Headings)
        writer.writeheader()
        writer.writerow(data)