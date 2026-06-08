# what is data structure
# the gave storage for daa so we can organize our data ans use it easily (save delete update)

# why we need data structure
# when we want to store multiple data into single varible

# name="mohit"

# print(name[0])

# name="mohit"

# print(name[4])

# name="mohit"

# print(name[2])

# name="mohit"
# a=len(name)
# print(a)

# name="mohitkumar"
# a=len(name)//2
# print(a)

# print calculate the vovals insie the name


# name="mohit kumar"
# a=len(name)
# print()

# for i in range("mohit kumar")
#    
name="mohitkumar"
i=0
count=0
while i<len(name):
    if(name[i]=='a' or name[i]=='e' or name[i]=='i' or name[i]=='o' or name[i]=='u'):
        count=count+1
    i=i+1    
print(count)

name="mohitkumar"
i=0
count=0
while i<len(name):
    if(name[i]!='a' or name[i]!='e' or name[i]!='i' or name[i]!='o' or name[i]!='u'):
        count=count+1
    i=i+1    
print(count)