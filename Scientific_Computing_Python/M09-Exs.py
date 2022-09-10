#Dictionaries Chapter
#https://books.trinket.io/pfe/09-dictionaries.html

#Ex2
days_data = {}

fname = input('Enter a file name: ')

for line in open(fname):
    if line.startswith('From '):
        new_line = line.split()
        days_data.update({new_line[2]:new_line[4]})

print(days_data)

#Ex3 
emails = {}

fname = input('Enter file name: ')

for line in open(fname):
    if line.startswith('From '):
        new_line = line.split()
        if new_line[1] in emails:
            emails[new_line[1]] += 1
        else:
            emails[new_line[1]] = 1
            
print('\n{}'.format(emails))

#Ex4 
emails = {}

fname = input('Enter file name: ')

for line in open(fname):
    if line.startswith('From '):
        new_line = line.split()
        if new_line[1] in emails:
            emails[new_line[1]] += 1
        else:
            emails[new_line[1]] = 1
            
print(emails)

#Ex5 
domain_emails = {}

fname = input('Enter file name: ')

for line in open(fname):
    if line.startswith('From '):
        new_line = line.split()
        domain = new_line[1].split('@')
        if domain[1] in domain_emails:
            domain_emails[domain[1]] += 1
        else:
            domain_emails[domain[1]] = 1
            
print(domain_emails)
        
            
