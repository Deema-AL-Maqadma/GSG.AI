print("****************************************")
import os #مكتبة جاهزة 
number=[]
if os.path.exists("prime.txt"):# للتحقق من وجود الملف
   with open("prime.txt","r") as f:
     #for line in f.readlines():دالة جاهزة بتقرا بيانات الملف كلها مرة وحدة
     for line in f:#لوب على البيانات في الملف تمشي سطر سطر
        data=line.strip()#  لازالة الفراغات لان بدي اضيفها للقائمة
        number.append(int(line))#نحولها من نص لرقم للتعامل معها 
     print(sum(number))
else  :
   print("File not exist")
print("****************************************")
#Exercise 1: Temperature Converter
#Write a function that takes a Celsius temperature and returns the Fahrenheit
#equivalent.
#Use input/output functions and function call.
#Save the result to a file.
def temp_convertor(cel):
   return cel*9/5 + 32
c=float(input("Enter thre tempreature :"))
fahrenheit=temp_convertor(c)
print("The fahrenheit = ",fahrenheit)
with open("temp.txt","w") as f:
   f.write(f"The fahrenheit = {fahrenheit}")
print("****************************************")
#Exercise 2: Grade Evaluator
#Read a list of student marks from a file (one mark per line).
#Calculate the average of the class.
#Display the average on the screen.
import os 
def calculate_average():
   if os.path.exists("prime.txt"):
      sum=0
      counter=0
      with open("prime.txt","r") as f:
         for line in f:
            grade=float(line.strip())
            sum+=grade
            counter+=1
         avg=sum/counter
         print("The Avarage = ",avg)
   else :
      print("Error! File not exist ...")
calculate_average()
print("****************************************")
#Exercise 3: Number Statistics
#Let the user enter a list of integers.
#Use loops to find max, min, count positives/negatives.
#Display summary in the console and write it to a file.
integer_str=input("Enter a list of integers separated by spaces : ")
numbers=[]
for x in integer_str.strip().split():
   numbers.append(int(x))
max_num = numbers[0]
min_num = numbers[0]
positive_count=0
negative_count=0
for num in numbers:
   if num>max_num:
      max_num=num
   if num<min_num:
      min_num=num
   if num>=0:
      positive_count+=1
   if num<0:
      negative_count+=1
informatin=(f"--->>> Information :\nMaximum : {max_num}\nMinmum : {min_num}\nPositive numbers : {positive_count}\nNegative Numbers : {negative_count}")
print(informatin)
with open("Information.txt","a") as f:
   f.write(informatin)
print("****************************************")
#Exercise 4: Login System
#Predefine usernames and passwords.
#Use a loop to validate user input.
#Use a function for validation.
#Log login attempts to a file.
username=["Deema","Ali"]
password=["123abc","ali"]
for i in range(len(username)):#لوب لكل الاسماء
   count=0
   while count!=3:
      name=input("Enter yor name : ")
      passw=input("Enter youe password : ")
      if name==username[i] and passw==password[i]:
         user_succ=(f"{username[i]} ---> login successfuly !\n")
         print(user_succ)
         with open("login.txt","a")as log:
            log.write(user_succ)
         break
      else:
         user_fail=(f"{username[i]} ---> login failed !\n")
         print(user_fail)
         with open("login.txt","a")as log:
            log.write(user_fail)
      count+=1
   if count==3:
               print("You are blocked !")
      
print("****************************************")
#Exercise 5: Recursive Calculator
#Implement a recursive function to calculate the power of a number (e.g., ab).
#Create a menu that allows the user to choose to calculate power, square, or exit
def power(base,exponant):
   if exponant==0:
      return 1
   return base*power(base,exponant-1)
while True :
   print(""" **** Welcome to Calculator ****
         1/ calculate power (a^b)
         2/ calculate square (a^2)
         3/ exit
         """)
   choice= input("Choose an operation : ")
   if choice=="1":
      a=int(input("Enter the base (a) : "))
      b=int(input("Enter the exponant (b) :"))
      result=power(a,b)
      print(f"{a}^{b} = {result}")
   elif choice=="2":
      a=int(input("Enter a number to square : "))
      result=power(a,2)
      print(f"{a}^{2} = {result}")
   elif choice=="3":
      print("Thx ...")
      break
   else:
      print("Invalid choice! please choose a valid option ...")

