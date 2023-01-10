#While loop 
from stat import FILE_ATTRIBUTE_SPARSE_FILE


i=0
while i<10:
    print("yes")
    i=i+1

#Write a program to print 1 to 50 using while loop
i=1
while i<51:
    print(i)
    i=i+1
    
#Write a program to print content of a list using loop.
l=[1,7,8]
i=0
while i<len(l):
    print(l[i])
    i=i+1

#for loop
fruits=["mango","grapes","watermelon","guava"]
for item in fruits:
    print(item)

#Range function in python
#example
for i in range (8):
    print(i)

for p in range(1,20,2):
    print(p)