# Deema Mohammed AL-Maqadma
#Q1/ Write Python ocode for checking if a year is a leap year
year=int(input("Enter The Year : "))
if(year%4==0 and year%100!=0)or year%400==0 :
    print("The Year",year,"is a Leap year")
else :
     print("The Year",year,"is NOT a Leap year")
print("*********************************")

# Deema Mohammed AL-Maqadma
#Q2/ Write a loop that prints the multiplication of a given number from user
number= int(input("Enter a number :"))
multiplier=1
while multiplier<=10 :
     print(number," * ",multiplier," = ",(number*multiplier))
     multiplier=multiplier+1