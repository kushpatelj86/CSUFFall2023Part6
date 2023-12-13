from locale import *

#question 8
value =123454345678987654.3234567
'{:,}'.format(value) 
f'{value:,}'
setlocale(LC_ALL,'')
f'{value:,}'          
num = format_string("%d", value, grouping=True)
print(num)


