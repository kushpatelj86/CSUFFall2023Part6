from string import Template
#question 4
t = Template('${village}folk send $$10 to $cause.')
t.substitute(village='Yorbq Linda', cause='Orange County')

#question 5
t.safe_substitute('e')



#question 6
class Percent(Template):
    def __init__(self,i_params,template):
        self.i_params = i_params
        self.template = template


    delimeter = '%'
    formt = input("Enter the syte(%d-date %n-seqnum %f-format):")
