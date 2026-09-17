# Function to convert the some token to upper case, lower case and capitalize the letter of some token
def word_modi(nw_text=list):
    modif_text = []
    
    x= 0 
    while x < len(nw_text):
        # validating the upper case
        if x+1 < len(nw_text) and nw_text[x+1] == "(up)":
            modif_text.append(str.upper(nw_text[x]))
            x+= 2
            # validating the lower case
        elif x+1 < len(nw_text) and nw_text[x+1]== "(low)":
            modif_text.append(str.lower(nw_text[x]))
            x+=2
            # validating the cap for capitalizing
        elif x+1 < len(nw_text) and nw_text[x+1] == "(cap)":
            modif_text.append(str.capitalize(nw_text[x]))
            x+=2 
        else:
            modif_text.append(nw_text[x])
            x+=1
    return modif_text