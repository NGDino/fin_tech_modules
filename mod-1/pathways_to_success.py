"""Pathways to Success."""
# @TODO: Import the Path tool from the pathlib library
# YOUR CODE HERE!
from pathlib import Path
import csv

# @TODO: Create a path to the `quarterly_data.csv` file
# YOUR CODE HERE!
csvpath = Path('Resources/quarterly_data.csv')

with open(csvpath) as csvfile:
    data = csv.reader(csvfile)
    for row in data:
        print(row)

# Print the relative path (the relative location of the file)
print(f"The relative CSV path is {csvpath}")

# Print the absolute path (The absolute location of the file on the computer)
print(f"The absolute CSV path is {csvpath.absolute()}")
