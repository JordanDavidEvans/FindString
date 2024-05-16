import re

def extract_ids(input_file, output_file):
    # Define the pattern to search for
    pattern = re.compile(r'"type":"Server","_id":"(.*?)"')

    # Initialize a list to store the found ids
    found_ids = []

    # Open the input file and search for the pattern
    with open(input_file, 'r') as file:
        for line in file:
            matches = pattern.findall(line)
            found_ids.extend(matches)

    # Write the found ids to the output file
    with open(output_file, 'w') as file:
        for _id in found_ids:
            file.write(_id + '\n')

# Specify the input and output file names
input_file = 'input.txt'
output_file = 'output.txt'

# Call the function to extract ids and write to the output file
extract_ids(input_file, output_file)
