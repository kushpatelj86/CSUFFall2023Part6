#1 list comprehension
squares =[x**2  for x in [1,2,3,4,5,6,7,8,9,10]]

print(squares)
#2
a = 2
b = 3
a,b = b,a
print(a,b)

#3
dd = {}

for i in "hello":
    dd[i] = "hello".count(i) 
 
print(dd)


#4

d =  [1,2,3,2,1,4,5,4]

for i in d:
    if d.count(i) > 1:
        d.remove(i)


print(d)
