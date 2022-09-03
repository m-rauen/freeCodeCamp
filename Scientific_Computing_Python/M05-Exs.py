#Ex01 
sum = 0
counter_elmnts = 0

while True:
    value = input('Enter a number: ')
    if value == 'done':
        break 
    else:
        try:
            value = float(value)
            counter_elmnts += 1
            sum += value
        except:
            print('Invalid input')
            continue

print('{:.0f} {:.0f} {:.2f}'.format(sum, counter_elmnts, sum/counter_elmnts))

#Ex02 
max_value = 0
min_value = None 

while True:
    value = int(input('Enter a number: '))
    if min_value == None:
        min_value = value
    elif value < min_value:
        min_value = value
    elif value > max_value:
        max_value = value  
    elif value == 'done':
        break 
    
print('Max: {}\n'
      'Min: {}'.format(max_value, min_value))