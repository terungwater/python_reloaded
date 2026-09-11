#creating a function that will work on both hex and bin
import token_1

changed_token = []
def hexandbin():
    word = "this guy is 1e (hex) years and the sister is 11 (bin) years"
    new_token = token_1.split(word)
    i =0 
    while i< len(new_token):
        if  i +1 < len(new_token) and new_token[i+1] == "(hex)":
            changed_token.append(int(new_token[i], 16))
            i+= 2
        elif i +1 < len(new_token) and new_token[i+1]=="(bin)":
            changed_token.append(int(new_token[i], 2))
            i += 2
        else:
            changed_token.append(new_token[i])
            i += 1
hexandbin()
print(changed_token)