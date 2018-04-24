import csv


# helper method to create a morse dictionairy from a csv file
# where the key is the morse code
def csv_to_dictionairy(csv_file, dictionairy):
    with open(csv_file, mode='r') as infile:
        reader = csv.reader(infile)
        dictionairy.update({rows[1]:rows[0] for rows in reader})

def text_to_morse(input, morse_dictionairy):
    output = ""
    split = input.split(" / ")
    for word in split:
        word = word.split(" ")
        for character in word:
            output += morse_dictionairy[character]
        output += " "
    return output


if __name__ == "__main__":
    morse_dictionairy = {}
    csv_to_dictionairy('morseDictionairy.csv', morse_dictionairy)

    text = text_to_morse(input(), morse_dictionairy)
    print(text)
