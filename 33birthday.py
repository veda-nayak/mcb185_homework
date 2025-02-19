import random 
import sys

# How to shake hands with everyone in the room

nums = [0, 1, 2, 3]

for i in range(0, len(nums)):
    for j in range(i+1, len(nums)):
        print(i,j)
        


# STEPS
# Create a classroom of random birthdays
# Empty list of students 
# Add students to the list
# Do any of the students have the same birthday
    # Add one person and check (faster) OR build the whole classroom and check
'''

n = 23

trials = 1000

for t in range(trials):
    peeps = []
    
    for i in range(n):
        bday = random.randint(0, 364)
       
'''       
        if bday in peeps:
            shared += 1
            break
        peeps.append(bday)   
 '''

''' 
        collision = False
        for i in range(0, len(peeps)):
            for j in range(1, len(peeps)):
                if peeps[i] == peeps[j]: collision = True
        
        if collision: shared += 1
'''

'''

# ANOTHER WAY

shared = 0
trials = 1000
days = 365
students = 23


for t in range(trials):
    # make an empty calender
    calendar = []
    for i in range(days):
        calendar.append(0)  # maek a list of 365 zeros

    # add student birthdays
    for i in range(students):
        bday = random.randint(0,days-1)
        calendar[bday] += 1 # go to the place that is that birthday and take it up by 1

    # check for shared birthdays

    collision = False
    for day in range(len(calendar)):
        if calendar[bday] > 1: 
            collision = True
            break
    
    if collision: shared += 1
    
print(shared/trials)
       
'''       
    # visually check for sharec birthdays    
    for n in calendar:
        symbol = None
        if n == 0: symbol = '_'
        elif n == 1: symbol = '.'
        else: symbol = '*'
        
        print(symbol, end = "")
        
        '''