#1

print("Values from 1 to n")
n=30
for (i) in range(1, n):
    print(i)


#2
print("Even Values from 1 to n")

for (i) in range(1, n):
    if i % 2 == 0:
        print(i)
    


#3

listjd = [ 1, 3, 6, 2, 6, 3, 4, 133, 24, 54, 782]
print("Even Values in the list")

for i in listjd:
    if i % 2 == 0:
        print(i)





#4

print("max value")

max = listjd[0]

for i in listjd:
    if i > max:
        max = i


print(max)


#5
print("Factorial")


def factorial(x):
    if x <= 1:
        return 1
    else:
        return (x) * factorial(x - 1)
    

print(factorial(5))
