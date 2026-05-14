import csv

with open("members.csv", newline="") as f:
    for row in csv.DictReader(f):
        print(row["first_name"], row["last_name"])
