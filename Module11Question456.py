from string import Template
#question 4
t = Template('${village}folk send $$10 to $cause.')
t.substitute(village='Yorbq Linda', cause='Orange County')

#question 5
t = Template('${village}folk send $$10 to $cause.')
print(t.safe_substitute(village='e'))



#question 6
class Percent(Template):



    delimeter = '%'
tremt = Percent("Hello, %name!")
print(tremt.substitute(name = 'james'))