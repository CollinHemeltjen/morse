import csv

# helper method to create a morse dictionairy from a csv file
# where the key is the normal character
def csv_to_dictionairy(csv_file, dictionairy):
    with open(csv_file, mode='r') as infile:
        reader = csv.reader(infile)
        dictionairy.update({rows[0]:rows[1] for rows in reader})

# uses the input and given dictionairy to find the corresponding morse code
def text_to_morse(input, morse_dictionairy):
    output = ""
    for character in input:
        output += morse_dictionairy[character.upper()] + " "

    return output


if __name__ == "__main__":
    morse_dictionairy = {}
    csv_to_dictionairy('morseDictionairy.csv', morse_dictionairy)

    morse = text_to_morse(input(), morse_dictionairy)
    print(morse)
