"""Q6. Write a function that reads in a CSV file and returns a list of dictionaries, where each dictionary represents
a row in the CSV file with the keys being the column names and the values being the cell values. """

import csv


def csv_to_dicts(file_path):
    with open(file_path, 'r') as f:
        reader = csv.DictReader(f)
        return list(reader)


path = 'CSVFile.csv'
print(csv_to_dicts(path))
