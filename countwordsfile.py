"""Write a Python program that takes a text file as input and returns the number of
words of a given text file.
Note: Some words can be separated by a comma with no space."""

f = open("demofile.txt","r")
read = f.read()
read.replace(","," ")
words=read.split(" ")
print("Number of words present in the file : ",len(words))