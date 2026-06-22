# set data structre 
# unordered
# indexing 
# unique data 
# faster for fing operation 
# set are also immutable


# double value ko hata deta ha ye
# st={1,2,2,3,3,4,5}
# print(st)

# data ko unique karke filter karta h or value ko change karta h 

# in not in -->membership operater
# print(6 in st)


# user={12,34,56,7,8,0}
# ans= {12,23,56,7,3,0}

# marks=0
# for x in user:
#     if (x in ans):
#         marks=marks+1

# print(marks)


user={12,34,56,7,8,0}
ans= {12,23,56,7,3,0}

marks=0
neg=1
for x in user:
    if (x in ans):
        marks=marks+1
    else:
        marks=marks-neg

print(marks)
    