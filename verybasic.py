import csv
import random

# Open the existing CSV file
with open("whatever.csv", "r") as file:
    reader = csv.reader(file)
    # Store the rows in a list
    rows = list(reader)

# Select 500 random rows
selected_rows = random.sample(rows, 500)

# Open a new file to save the selected rows
with open("new.csv", "w", newline='') as new_file:
    writer = csv.writer(new_file)
    # Write the selected rows to the new file
    writer.writerows(selected_rows)
