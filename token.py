#; function the split input
def split(input):
    punc = ",.!?:;"
    list_of_token = []
    words = ""
    i = 0
    while i < len(input):
        char = input[i]
        if char == " ":
            if words:
                list_of_token.append(words)
                words =""
        elif char =="(":
            if words:
                list_of_token.append(words)
                words = ""
        endpoint = input.find()
        # validating punctuation marks
        elif char in punc:
            if words:
                list_of_token.append(words)
                words =""
            list_of_token.append(char)
        else:
            words+= char
        i += 1
    #appending the last token to the list
    if words:
        list_of_token.append(words)
    return list_of_token
print(split("If I must choose between two evils, I'd rather not choose at all (up). 1E (hex) files were found. 10 (bin) errors occurred."))