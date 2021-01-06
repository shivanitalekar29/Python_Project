from datetime import date

#Write a Python program to calculate the number of days between two dates.

a=date(2021,1,5)
b=date(2021,1,1)

delta = a-b
print(delta.days,"days")
