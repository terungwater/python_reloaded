import sys

def main_func():
    input = sys.argv[1]
    output = sys.argv[2]
    with open(input) as infile:
        content = infile.read()
    with open(output, "w") as outfile:
        output_content = outfile.write(content)
    return output_content
main_func()