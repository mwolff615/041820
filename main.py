'''#day 1 

#pre-course survey
    #https://docs.google.com/forms/d/1sLm3W-IT1SON14nHPcDX5AggjQDL6GF6a0khNXpbvMc/viewform?edit_requested=true

#repository 
#done :) 

#print statements 
print("hello world")
print('hello world')
print("Epic")

#anything in quotes is a string

#printing numbers 
print(17)
print(111)

#assign your variable before using it 
a = 'this is a message'
print(a)

print('111')

print("hello " + "world") #concatenation 

print("100" + "one hundred")

#+ with numbers -> adds the numbers
#+ with strings -> concatenates them 

print(str(100) + "one hundred")

print(100 / 600)

#math in python 
#+ -> addition 
#- -> subtraction 
#/ -> float division 
#// -> integer division 
#% -> modulus 
#* -> multiplication 
#** -> exponentiation 

#float division keep all the decimal places
print(100/8)

#truncates decimal 
print(100//8)

#modulus
#12 remainder 4 (the remainder you get after division)
print(100%8)

print(1%4)

#exponentiation 
print(10**2)
print(10*10)

print(8**3)
print(8*8*8)

print(12**0)


#''
#""

#escape characters 
print("\t what does this do?")
#don't print the t, but use it to make a tab
print("what about \n this")
#makes a new line


print("With this stradegy, \nI will make a GREAT\n\tRPG!")

#definitions 
    #program - list a sequential instructions for a computer to execute 
    #computational thinking - the approach of breaking problems down into smaller subproblems and writing algorithms to solve those subproblems 
    #computer science - the study of using computational approaches 
    #algorithms - ordered list of instructions 
    #pseudocode - not real code, but gives you an idea of how to write the code 

    #show the user the number 100 
print(100)

    #print a very long number 
print(1000000000000000)

    #program flow - what order things happen in your program/code - usually top to bottom 

    #IPO - input-process-output 

#input-process-output 
x = int(input("enter a number: "))
y = x + 10
print("your number plus 10: " + str(y))

name = str(input("What is your name? "))
print("Your name is " + name)'''

#comment
#line 106

#Almost Day 2
print('x')

#can do this to avoid having to comment everything out 
import os 
os.system('clear')

userNumber = int(input("Enter a number:"))

#conditionals 
if(userNumber == 10): 
    print("Your number is 10")
else: 
    print("Your number is not 10")

if(userNumber == 80):
    print("80 is epic")
else:
    if(userNumber == 0):
        print("the void")
    else:
        print("You didn't put a lucky number")

#Day 2 (for real)