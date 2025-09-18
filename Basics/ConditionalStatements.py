#Conditions and operators:
score=float(input("Enter the score : "))
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("C or below")
print("*********************************************")
#Q1/Compare two numbers and print the greater
num1=int(input("Enter the num1 :"))
num2=int(input("Enter the num2 :"))
greater=None
if num1>num2:
    greater=num1
    print("The greater = ",greater)
else:
    greater=num2
    print("The greater = ",greater)
print("*********************************************")
#Q2/Check if a character is inside a string or not.
string=("Hello World !")
if "!" in string :
    print ("Yes")
print("*********************************************")
#Q3/Create a condition where a user is granted access only if both the username and password match predefined values
username = input("Enter username: ")
password = input("Enter password: ")
if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid credentials")
