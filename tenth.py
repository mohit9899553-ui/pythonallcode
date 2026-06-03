# main function
# aaaaa?a

def Add(a,b):
    return a+b

def Sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if(b==0):
        print('infinty')
    else:
        return a/b
    

# def Clac():
#     num1=int(input('enter the first number '))
#     num2=int(input('enter the second number '))
#     op=input('enter operator ')

#     if(op=='+'):
#         print(Add(num1,num2))
#     elif(op=='-'):
#         print(Sub(num1,num2))
#     elif(op=='*'):
#         print(mul(num1,num2))
#     elif(op=='/'):
#         print(div(num1,num2))

# Clac()

# def main():
#     num1=int(input('enter the first number '))
#     num2=int(input('enter the second number '))
#     op=input('enter operator ')

#     if(op=='+'):
#         print(Add(num1,num2))
#     elif(op=='-'):
#         print(Sub(num1,num2))
#     elif(op=='*'):
#         print(mul(num1,num2))
#     elif(op=='/'):
#         print(div(num1,num2))

# main()

# def Add(a,b):
#     return a+b

# def Sub(a,b):
#     return a-b

# def mul(a,b):
#     return a*b

# def div(a,b):
#     if(b==0):
#         print('infinty')
#     else:
#         return a/b
    

# def main():
#     num1=int(input('enter the first number '))
#     num2=int(input('enter the second number '))
#     op=input('enter operator ')

#     if(op=='+'):
#         print(Add(num1,num2))
#     elif(op=='-'):
#         print(Sub(num1,num2))
#     elif(op=='*'):
#         print(mul(num1,num2))
#     elif(op=='/'):
#         print(div(num1,num2))
#     else:
#         print('valid number of operter ')



for x in range(1,100):
    if(x%2!=0):
        print('even',x)