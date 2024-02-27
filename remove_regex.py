import csv
import re
import sys

def remove_regular_expression(line):
    #@@...@@
    pattern = r'@@.*?@@'
    new_line = re.sub(pattern, '', line)
    return new_line

def remove_expression_from_csv(input, output):
    with open(input, 'r', newline='') as input_file, open(output, 'w', newline='') as output_file:
        csv_reader = csv.reader(input_file)
        csv_writer = csv.writer(output_file)

        for line in csv_reader:
            new_line = [remove_regular_expression(column) for column in line]
            csv_writer.writerow(new_line)


if len(sys.argv) != 3:
    print(""" Wrong number of parameters! Use: python remove_regex.py <input_file_path> <output_file_path>""")
    sys.exit(1)

p1 = sys.argv[1]
p2 = sys.argv[2]

input_file = p1
output_file = p2    
remove_expression_from_csv(input_file, output_file)