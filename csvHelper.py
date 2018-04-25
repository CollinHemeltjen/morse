import csv

# helper method to create a morse dictionairy from a csv file
# where the key is the morse code
def csv_to_dictionairy_morse(csv_file, dictionairy):
    with open(csv_file, mode='r') as infile:
        reader = csv.reader(infile)
        dictionairy.update({rows[1]:rows[0] for rows in reader})

# helper method to create a morse dictionairy from a csv file
# where the key is the normal character
def csv_to_dictionairy_text(csv_file, dictionairy):
    with open(csv_file, mode='r') as infile:
        reader = csv.reader(infile)
        dictionairy.update({rows[0]:rows[1] for rows in reader})
