import csvHelper



# uses the input and given dictionairy to find the corresponding morse code
def text_to_morse(input, morse_dictionairy):
    output = ""
    for character in input:
        output += morse_dictionairy[character.upper()] + " "

    return output


if __name__ == "__main__":
    morse_dictionairy = {}
    csvHelper.csv_to_dictionairy_text('morseDictionairy.csv', morse_dictionairy)

    morse = text_to_morse(input(), morse_dictionairy)
    print(morse)
