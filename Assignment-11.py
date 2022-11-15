# 1. Write a python script to calculate sum of first N natural numbers
'''userInput = int(input("Enter Number : "))
sum = 0
for i in range(1,userInput+1):
    sum+=i
print(sum)'''

# 2. Write a python script to calculate sum of squares of first N natural numbers
'''userInput = int(input("Emter Number : "))
outsum = 0
for i in range(1,userInput+1):
    insum = (i*i) #1,4,9,16,25
    outsum+=insum
print(outsum)'''

# 3. Write a python script to calculate sum of cubes of first N natural numbers
'''userInput = int(input("Emter Number : "))
outsum = 0
for i in range(1,userInput+1):
    insum = (i**3) #1,8,27,64,125
    outsum+=insum
print(outsum)'''

#4. Write a python script to calculate sum of first N odd natural numbers
'''userInput = int(input("Emter Number : "))
outsum = 0
insum = 0
for i in range(1,userInput+1): #1,3,5,7,9
    if(i%2!=0):
        insum+=i
        outsum = insum    
print(outsum)'''

#5. Write a python script to calculate sum of first N even natural numbers
'''userInput = int(input("Emter Number : "))
outsum = 0
insum = 0
for i in range(1,userInput+1): #1,3,5,7,9
    if(i%2==0):
        insum+=i
        outsum = insum    
print(outsum)'''

#6. Write a python script to calculate factorial of a given number 1 × 2 × 3 × 4 × 5 × 6 × 7
'''userInput = int(input("Emter factorial Number : "))
infact = 1
for i in range(1,userInput+1):
    infact*=i #infact = infact*i
    
print(infact)'''

# 7. Write a python script to count digits in a given number
'''userInput = int(input("count digits : "))
count = 0
while(userInput):
    userInput//=10
    count+=1
print(count)   ''' 

# 8. Write a python script to calculate sum of digits of a given number
'''userInput = int(input("calculate sum of digits : "))
userInput = str(userInput)
sum = 0

for i in userInput:
    sum+= int(i)
print(sum)'''

#9 Write a python script to print binary equivalent of a given decimal number. (do notuse bin() method)
'''print('{0:b}'.format(int(5)))'''
# Write a python script to print the octal equivalent of a given decimal number. (do notuse oct() method)
'''num = 15
print('%o'%num)'''


