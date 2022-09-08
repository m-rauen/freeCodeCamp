#Strings Chapter

#Ex05
str = 'X-DSPAM-Confidence: 0.8475'

value = str.find(':')
number = str[value+1:]
number = float(number)
print(number)






