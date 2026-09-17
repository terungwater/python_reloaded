#creating a function that will work on both hex and bin

def hexandbin_func(new_token):
    changed_token = []
    i =0 
    while i< len(new_token):
        #converting the token to base 16
        if  i +1 < len(new_token) and new_token[i+1] == "(hex)":
            changed_token.append(int(new_token[i], 16))
            i+= 2
            # validating the bin to convert it to base 2 
        elif i +1 < len(new_token) and new_token[i+1]=="(bin)":
            changed_token.append(int(new_token[i], 2))
            i += 2
        else:
            # adding the other tokens to the list
            changed_token.append(new_token[i])
            i += 1
    return changed_token