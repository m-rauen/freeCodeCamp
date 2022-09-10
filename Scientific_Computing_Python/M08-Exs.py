#Arrays Chapter
#https://books.trinket.io/pfe/08-lists.html

#Ex4 
arr_words = []

file_input = input('Enter file: ')

for lines in open(file_input):
    new_lines = lines.rstrip()
    separated_words = new_lines.split()
    for w in separated_words:
        if w in arr_words:
            continue
        else:
            arr_words.append(w)

print(sorted(arr_words))

#Ex5 
count_lines = 0
email_arr = []

file_name = input('Enter a file name: ')

for line in open(file_name):
    if line.startswith('From '):
        new_lines = line.split()
        print(new_lines[1])
        count_lines += 1
        
print("There were {} lines in the file with 'From' as the first word".format(count_lines))

#Ex6 
all_values = []

while True:
    value = input('Enter a number: ')

    if value == 'done':
        break
    else:
        all_values.append(value)
    
print('Maximum: {:.1f}'.format(float(max(all_values))))
print('Minimum: {:.1f}'.format(float(min(all_values))))


        

