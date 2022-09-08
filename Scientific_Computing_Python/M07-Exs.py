#Files Chapter

#Ex01 
fname = input('Enter a file name: ')

for lines in open(fname):
    print(lines.upper())

#Ex02 
fname = input('Enter a file name: ')
sum_values = 0
counter_values = 0

for lines in open(fname):
    if lines.startswith('X-DSPAM-Confidence'):
        line = lines.rstrip()
        split_value = line.find(': ')
        value = float(line[split_value+2:])
        sum_values += value
        counter_values += 1     

print('Average spam confidence: {}'.format(sum_values / counter_values))

#Ex03 
counting_subjects = 0

fname = input('Enter a file name: ')

if fname == 'na na boo boo':
    print("NA NA BOO BOO TO YOU - You have beem punk'd")
    quit()
else:
    try:
        for lines in open(fname):
            if lines.startswith('Subject'):
                counting_subjects += 1
                continue         
    except:
        print('File cannot be opened: {}'.format(fname))
        quit()
        
print('There were {} subject lines in {}'.format(counting_subjects, fname))