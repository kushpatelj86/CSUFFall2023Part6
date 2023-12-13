from pprint import *
from textwrap import *
import locale


#question 1
list1=[[1,2,3],[4,5,6],[7,8,9]]


pprint(list1,width=30,indent=10)

#question 2
string1 = "As a result, Portuguese is now the official language of several independent countries and regions: Angola, Brazil, Cape Verde, East Timor, Guinea Bissau, Macau, Mozambique, Portugal, & São Tomé and Príncipe. "
wrap(string1, width=50)


#question 3
locale.setlocale(locale.LC_ALL,'English_United States.1252')

format = locale.format_string("%s%.*f",( locale.localeconv()['currency_symbol'], 2, 1234567.89), grouping=True)
print(format)








