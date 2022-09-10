#Tuples Chapter
#https://books.trinket.io/pfe/10-tuples.html

#Ex1 
def reverse_data(gross_dt):
    ordered_data = []
    for k,v in gross_dt.items():
        ordered_data.append((v,k))
    
    return ordered_data

data = {}

filename = input('Enter a file name: ')

for line in open(filename):
    if line.startswith('From '):
        words = line.split()
        if words[1] in data:
            data[words[1]] += 1
        else:
            data[words[1]] = 1

ord_data = reverse_data(data)
    
final_data = sorted(ord_data, reverse=True)
for count, email in final_data[:1]:
    print(email, count)
    
#Ex2 
count_hours = {}
ordered_data = []

filename = input('Enter a file name: ')

for line in open(filename):
    if line.startswith('From '):
        words = line.split()
        hour = (words[5]).split(':')
        if hour[0] in count_hours:
            count_hours[hour[0]] += 1
        else:
            count_hours[hour[0]] = 1
            
for k,v in count_hours.items():
        ordered_data.append((k,v))

for time, count in sorted(ordered_data):
    print(time, count, end='\n')

#Ex3 
def handle_file(fname):
    count_words = {}
    total_words = 0
    
    for lines in open(fname):
        for words in lines.lower():
            if words.isalpha() == True:
                total_words += 1
                if words not in count_words:
                    count_words[words] = 1
                else:
                    count_words[words] += 1
    
    return count_words, total_words

def reverse_data(normal):
    inverse = []
    
    for k,v in normal.items():
        inverse.append([v,k])
    
    return inverse

def calculate_frequency(raw_numbers, total):
    final_order = []
    
    for value, key in raw_numbers:
        freq_value = (value/total)*100
        final_order.append([freq_value, key])        
    
    return final_order

filename = input('Enter a file name: ')
words, tot_words = handle_file(filename)
inv_words = reverse_data(words)
final_order = calculate_frequency(inv_words, tot_words)

for val, key in sorted(final_order, reverse=True):
    print('{} {:.2f}'.format(key, val), end='\n')




                

    
    

    
    


    


    