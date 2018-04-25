import csvHelper




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
    csvHelper.csv_to_dictionairy_morse('morseDictionairy.csv', morse_dictionairy)

    text = text_to_morse(input(), morse_dictionairy)
    print(text)
