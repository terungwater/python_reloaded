import sys
import token_1
import hexandbin
import word_modi

# function for processing the other functions for result
def main_func():
    input = sys.argv[1]
    output = sys.argv[2]
    # openning and reading the files for the processing 
    with open(input) as infile:
        content = infile.read()
        new_content = token_1.split(content)
        checked_content = hexandbin.hexandbin_func(new_content)
        word_content = word_modi.word_modi_func(checked_content)
        converted_content = " ".join(map(str, word_content))
    # openning the file to write to 
    with open(output, "w") as outfile:
        output_content = outfile.write(converted_content)
    return output_content
print("Processing...")
main_func()