#Ex01
hours = float(input('Enter hours: '))
rate = float(input('Enter rate: '))

if hours > 40:
    ot_hours = hours - 40.0
    ot_rate = 1.5 * rate
    ot_payment = ot_hours * ot_rate
    gross_payment = (40 * rate) + ot_payment
    print('Pay: {}'.format(gross_payment))
elif hours <= 40:
    gross_payment = hours * rate
    print('Pay: {}'.format(gross_payment))

#Ex02 
hours = input('Enter hours: ')
rate = input('Enter rate: ')
try:
    hours = float(hours)
    rate = float(rate)
except:
    print('Error, please enter numeric input')    

if hours > 40:
    ot_hours = hours - 40.0
    ot_rate = 1.5 * rate
    ot_payment = ot_hours * ot_rate
    gross_payment = (40 * rate) + ot_payment
    print('Pay: {}'.format(gross_payment))
elif hours <= 40:
    gross_payment = hours * rate
    print('Pay: {}'.format(gross_payment))

#Ex03 
score = float(input('Enter score: '))

if score > 1:
    print('Bad score')
else:
    if score >= 0.9:
        print('A')
    elif 0.8 <= score < 0.9:
        print('B')
    elif 0.7 <= score < 0.8:
        print('C')
    elif 0.6 <= score < 0.7:
        print('D')
    else:
        print('F')
