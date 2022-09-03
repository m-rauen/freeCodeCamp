#Ex06
# def computepay(hours, rate):
#     if hours > 40:
#         ot_hours = hours - 40
#         ot_rate = rate + (0.5 * rate)
#         ot_payment = ot_hours * ot_rate 
#         normal_payment = rate * 40
#         gross_payment = ot_payment + normal_payment
#         return gross_payment
#     elif hours <= 40:
#         gross_payment = hours * rate 
#         return gross_payment
        
        

# hours = float(input('Enter hours: ') )
# rate = float(input('Enter rate: '))
# computepay(hours, rate)

#Ex07 
def computegrade(value):
    if value > 0.9:
        print('A')
    elif 0.8 < value < 0.9:
        print('B')
    elif 0.7 < value < 0.8:
        print('C')
    elif 0.6 < value < 0.7:
        print('D')
    elif value <= 0.6:
        print('F')


score = input('Enter score: ')
score = float(score)
if score > 1.0:
    print('Bad score')
else:
    computegrade(score)





