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
