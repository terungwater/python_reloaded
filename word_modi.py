
import token_1

modi_text = []
def word_modi():
    text = "he (up) is above any other GOD (low)"
    nw_text = token_1.split(text)

    x= 0 
    while x < len(nw_text):
        if x+1 < len(nw_text) and nw_text[x+1] == "(up)":
            modi_text.append(str.upper(nw_text[x]))
            x+= 2
        elif x+1 < len(nw_text) and nw_text[x+1]== "(low)":
            modi_text.append(str.lower(nw_text[x]))
            x+=2
        else:
            modi_text.append(nw_text[x])
            x+=1
word_modi()
print(modi_text)