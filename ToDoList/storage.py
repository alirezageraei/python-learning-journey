import csv

def save_data(data):
    
    # saves all data in a CSV list, line by line.
    with open("tasks.csv", "w",newline="") as t:
        
        Headings = ["name", "discription", "priority"]
        writer = csv.DictWriter(t, fieldnames=Headings)
        writer.writeheader()
        for item in data:
            writer.writerow(item)

# def load_data(file_name):

#     while True:
#         # Loads data Line by line from a CSV file
#         try:    
#             with open(file_name, "r", newline='') as t:
#                 reader = csv.DictReader(t, csv)
#                 for row in reader:

#             break 
#         except FileNotFoundError:
#             print(f"Please enter a valid file path, {file_name} not found")
#             continue        