#Write a Python program to read a file line by line and store it into a list
f = open("demofile.txt","r")

for x in f:
    print(x)

a=f.readlines()
b=list(f)
print(type(a))
print(type(b))



