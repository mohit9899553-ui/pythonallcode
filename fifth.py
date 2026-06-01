# name=input('Enter your name: ')
# if(name=='rohit'):
#    print('trainer a madrid')
# else:
#     print('student at madird') 

# marks=input('Enter the marks obtined')
# if(marks==98):
#    print('pass')
# else:
#    print('fail')


# algorithms
# steps of instruction to achieve a spefic goal/task problem solve

# take input of age from the user and print whether he can vote in india or not

# age=int(input('what is your age:?'))

# if(age>=20):
#    print('yes you can vote')
# else:
#    print('no you can did not wait')

# marks=int(input('how much you obtained'))

# if(marks>=38):
#    print('you are pass')
# else:
#    print('you are fail')    
## Problem 1: Age Eligibility and Type Conversion

# Ask the user to enter their birth year as a string. Convert it to an integer and calculate their age (assume the current year is 2026). Using comparison and logical operators, check if the person is both:

# * 18 years or older
# * Age less than or equal to 60
#   Print the age and whether the person is in the “working age group”.


# birthYear=int(input('what is your birth year'))
# currentyear=2026 
# age=birthYear-currentyear
# if(age>=18 and age<=60):
#    print('working age group')
# else:
#     print('not working age group')  

   # Take the price and quantity of an item as input from the user. 
   #  Convert them to appropriate numeric types and calculate the total amount. If the total amount
   #   is greater than 1000 *and* quantity is more than 5, apply a 10% discount. Otherwise, 
   #   print the normal total. Display final payable amount.

# price=int(input('tell me your price'))
# quantity=int(input('how much you buyed'))
# totalbill=price*quantity
# if(price>1000 and quantity>5):
#   discount=(10/100)*totalbill
#   grandtotal=totalbill-discount
#   print('yaa you got the discount',grandtotal)
# else:
#    print('you did not get the discount',totalbill)
#    Problem 3: Student Percentage and Pass/Fail Decision


# maths=int(input('how much marks you obtained'))
# science=int(input('how much marks you obtained'))
# sst=int(input('how mush marks you obtained'))
# obtainedmarks=maths+science+sst
# totalmarks=300
# percentage=totalmarks/3*300
# if(percentage>40 and maths>33 and science>=33 and sst>=33):
#    print('pass')
# else:
#    print('fail')

# num1=int(input())
# num2=int(input())
# if(num1>num2):
#    print('num1 is greater then num2')
# else:
#    print('num2 is greater then num1')

# Problem 4: Number Comparison with Arithmetic Result

# Ask the user to input two numbers. Perform arithmetic operations (addition and
#  multiplication). Then compare:

# * Check if the sum is greater than the product *or* if both numbers are equal
#   Print appropriate messages using logical and comparison operators.

# number1=int(input())
# number2=int(input())
# addition=number1+number2
# multiplication=number1*number2
# if(addition>multiplication):
#    print('addition is greater')
# elif(addition<multiplication):
#    print('multiplication is greater')
# else:
#    print('both are equal')
# Problem 5: BMI Category Checker

# Ask the user to input their weight (kg) and height (meters). Convert inputs to 
# floats and calculate BMI using the formula:
# BMI = weight / (height * height)
# Using comparison and logical operators, print whether the person is:

# * Underweight (BMI < 18.5)
# * Normal (BMI between 18.5 and 24.9)
# * Overweight (BMI ≥ 25)
#   Also print the calculated BMI.

# height=float(input())
# weight=float(input())

# bmi=weight/(height*height)
# if(bmi<18.5 and bmi>24.9):
#   print('normal')
# elif(bmi>=25):
#    print('Overweight')
# else:
#    print('underwieght')

# roblem 6: Loan Eligibility

# Ask the user to input their monthly income and age. Convert to integers. 
# Using arithmetic, comparison, and logical operators determine if the user is eligible for a loan:
# Conditions:

# * Age between 21 and 60
# * Income greater than or equal to 25000
#   Print whether the person is eligible or not.

# monthlyincome=int(input(' enter your income '))
# age=int(input(' enter your age '))
# if(monthlyincome>25000 and age<21 and age>60):
#    print('eligible')
# else:
#    print('not')

# Problem 7: Calculator with Condition Check

# Take two numbers as floats and an operator (+, -, *, /) as input. Perform the 
# corresponding arithmetic operation. Before division, check using comparison
# operators that the second number is not zero. Use logical operators where  needed 
# and print the result.

# num1=float(input())
# num2=float(input())
# optertar=input()

# if(optertar=='+'):
#    print(num1+num2)
# elif(optertar=='-'):
#    print(num1-num2)
# elif(optertar=='*'):
#    print(num1*num2)
# else:
#    if(num2!=0):
#       print(num1/num2)
#    else:
#       print('divison is not possible')

# Problem 8: Electricity Bill Calculator

#  
#       surcharge=5/100*totalbill
#       grandtotal=totalbill+surcharge
#       print('here is your bill', grandtotal)
#      else:
#       print('here is your bill', totalbill)
# else:
#    aftertwohundred=unit-200
#    totalbill=5*100+7*100+aftertwohundred*10
#    if(totalbill>1500 or unit>200):
#      surcharge=5/100*totalbill
#      grandtotal=totalbill+surcharge
#      print('your bill is', grandtotal)
#    else:
#       print('your bill is', totalbill)
# ask the user to enter their current salary (float) and performance rating (out of 5).
# If rating is greater than or equal to 4 and salary is less than 80000, 
# # increase salary by 15%; otherwise increase by 5%. Then check using
# comparison and logical operators whether the new salary is taxable 
# (greater than 50000). Print old salary, new salary, and taxability status.

# salary=float(input('Enter your current salary'))
# rating=int(input('Enter your rating'))

# if(salary<80000 and rating>=4):
#    hike=15/100*salary
#    totalsalary=salary+hike
#    if(totalsalary>50000):
#       print



# Problem 10: Voting Booth Validator

# Take age and city name as input. Convert age to integer. Using logical 
# operators, verify that the person is at least 18 and does not live in a
#  restricted city named "TestCity". Print whether they can vote in the local
#   booth. Also print how many years are left if they are underage (use arithmetic operator).

# age=int(input('Enter your age'))
# city=input('Enter your city name')
# TestCity='kolkata'
# if(age>=18 and city!=TestCity):
#    print('you can vote here')
# else:
#    if(age<18):
#      print('you are vote here', 18-age)
#    else:
#       ('you cannot vote')


# side1=float(input('enter the side 1'))
# side2=float(input('enter the side 2'))
# side3=float(input('enter the side 3'))

# if(((side1+side2>side3)or(side2+side3>side1)or(side3+side2>side1))and(side1!=0 and side2!=0 and side3!=0)):
#    print('valid trinagle')
#    if(side3==side2 and side1==side3):
#       print('equilateral')
#    elif(side1==side2 or side2==side3 or side1==side3):
#       print('isosacle')
#    else:
#       print('scalene')
# else:
#    print('not a valid triangle')

# Ask the user to input total data used in GB (float). Convert if required. Calculate the
#  base bill at 50 per GB.If usage is greater than 10 GB and less than or equal to 25 GB,
#   give 8% discount;
#   if greater than 25 GB, give 12% discount. Also add 18% tax if final amount is 
#   greater than 1000 using logical operators. Print usage and final bill

# datause=float(input('how much data use'))
# basebill=datause*50

# if(datause>10 and datause<=25):
#    discount1=8/100*basebill
#    grandtotal1=discount1+basebill
#    print(grandtotal1)
# elif(datause>25 and basebill>1000):
#       discount2=12/100*basebill
#       gst=18/100*discount2
#       grandtotal2=gst+discount2
#       print(grandtotal2)
# else:
   # print(grandtotal2)

# data=float(input('Enter your unit '))
# totalbill=0
# discount=0
# if(data>10 and data<=25):
#    totalbill=data*50
#    discount=8/100*totalbill
#    finalbill=totalbill-discount
#    if(totalbill>1000):
#       gst=18/100*totalbill
#       gstbill=finalbill+gst
#       print('bill',gstbill)
#    else:
#       print('bill',finalbill)
# elif(data>25):
#    totalbill=data*50
#    discount=12/100*totalbill
#    finalbill=totalbill-discount
#    gst=18/100*totalbill
#    gstbill=gst+finalbill
#    print('bill',gstbill)
# else:
#    totalbill=data*50
#    print('bill:',totalbill)   

#F=(C x 1.8)+32

# Problem 13: Temperature Converter and Weather Check

# Take temperature input in Celsius as a string, convert it to float, and convert 
# it to Fahrenheit using arithmetic operators. Using comparison and logical operators,
# print whether the weather is cold (≤ 15), pleasant (16–30), or hot (> 30). Also print 
# both Celsius and Fahrenheit values.

# celsius=float(input('Enter your temperature'))
# Fahrenheit=(celsius*1.8)+32
# if(Fahrenheit<=15):
#    print('wheather is cold')
# elif(Fahrenheit>=16 and Fahrenheit<30):
#       print('wheather us pleasent')
# else:
#    print('wheather is hot')    

zzz  







   







