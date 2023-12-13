#part 1
def greet(name, msg):
    return msg + " " + name + "!"


#part2
def swap(a, b):
    temp = a
    a = b
    b = temp


#part3
def rectangle_area(length, width):
    return length * width 





#part 4

def average(*args):
    sum = 0
    for i in args:
        sum += i

    average = sum /len(args)
    return average




def build_profile(name, job="student"):
    profiles ={"Harry" : job, "Marry" : job, "Larry" : job,"Terry" : job}
    return profiles    


nums1 = [1, 2, 3] 
nums2 = [4, 5, 6] 
data = {"x": 10, "y": 20} 

def unpacking_example(a, b, c, x=data["x"], y=data["y"]):
    sum = 0
    a = nums1[0]
    b = nums1[1]
    c = nums1[2]

    a += nums2[0]
    b += nums2[1]
    c += nums2[2]
    
    sum = a + b + c + x + y



sum = lambda a,b: a + b

 




numbers = [("James",18),("Ethan",20),("William",21),("Chris",32)]


sorted = lambda numbers : sorted(numbers)