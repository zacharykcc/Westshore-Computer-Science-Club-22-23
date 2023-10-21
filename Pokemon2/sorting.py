# Open the input file for reading
with open('output.txt', 'r') as input_file:
    # Read all the lines from the input file
    lines = input_file.readlines()

# Extract the first number from each line and store it in a list
numbers = [int(line.split()[0]) for line in lines]

# Sort the list in descending order
numbers.sort(reverse=True)

# Open the output file for writing
with open('output2.txt', 'w') as output_file:
    # Write each number to the output file, followed by a newline character
    for number in numbers:
        output_file.write(str(number) + '\n')
