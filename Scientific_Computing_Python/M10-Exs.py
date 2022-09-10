#Tuples Chapter
#https://books.trinket.io/pfe/10-tuples.html

#Ex1 
# def reverse_data(gross_dt):
#     ordered_data = []
#     for k,v in gross_dt.items():
#         ordered_data.append((v,k))
    
#     return ordered_data

# data = {}

# filename = input('Enter a file name: ')

# for line in open(filename):
#     if line.startswith('From '):
#         words = line.split()
#         if words[1] in data:
#             data[words[1]] += 1
#         else:
#             data[words[1]] = 1

# ord_data = reverse_data(data)
    
# final_data = sorted(ord_data, reverse=True)
# for count, email in final_data[:1]:
#     print(email, count)
    
#Ex2 
# count_hours = {}
# ordered_data = []

# filename = input('Enter a file name: ')

# for line in open(filename):
#     if line.startswith('From '):
#         words = line.split()
#         hour = (words[5]).split(':')
#         if hour[0] in count_hours:
#             count_hours[hour[0]] += 1
#         else:
#             count_hours[hour[0]] = 1
            
# for k,v in count_hours.items():
#         ordered_data.append((k,v))

# for time, count in sorted(ordered_data):
#     print(time, count, end='\n')

#Ex3 
def handle_file(fname):
    count_words = {}
    for lines in open(fname):
        for words in lines.lower():
            if words.isalpha() == True:
                if words not in count_words:
                    count_words[words] = 1
                else:
                    count_words[words] += 1
    
    return count_words

organize_words = []

filename = input('Enter a file name: ')
words = handle_file(filename)




                

    
    

    
    


    


    