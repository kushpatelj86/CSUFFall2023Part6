# main.py
def two_sum(nums, target):
    # WRITE YOUR LOGIC HERE
    
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i , j]
           

                 
                 
   

    

def length_of_last_word(s):
    # WRITE YOUR LOGIC HERE
    tempString = ""

    for c in s[::-1]:
        if c == ' ' and len(tempString) != 0:
            break
        if c != ' ':
        
            tempString += c
            
    return len(tempString)
    

def search_insert(nums, target):
    # WRITE YOUR LOGIC HERE
    
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    
    nums.append(target) 
    nums.sort()

    
    for i in range(len(nums)):
        if nums[i] == target:
            return i

    

    
    
