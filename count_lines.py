import pandas as pd

def count_lines(string):
    lines = string.splitlines()
    number_of_lines = len(lines)
    return number_of_lines

df = pd.read_csv('cleaned_diff_hunk.csv')
all_diff_lines = []

for index, row in df.iterrows():
    diff_lines = count_lines(row['cleaned_diff_hunk'])
    all_diff_lines.append(diff_lines)

df['diff_lines'] = all_diff_lines

print(df.head())

df.to_csv('filtered_by_number_of_lines.csv', index=False)

# number = 0
# for index, row in df.iterrows():
#     if (row['diff_lines'] == 1):
#         number +=1

# print(number)