# : Function Definitions and Types :
#Function without parameters and no return:القراءة والطباعة بنفس الميثود
def say_hello():
    print("Hello!")
say_hello() #call to the function to execute
#Function with parameters but no return: تعديل على قيمة وطباعة الناتج
def greet_user(name):
    print("Hello,", name)
greet_user("Ali")
#Function with parameters and a return value:
def add(a, b):
    return a + b
result = add(3, 5) #ترجع بقيمة بخزنها داخل متغير وتكون الطباعة خارج الميثود
print(result)
#Function without parameters but with return:
def get_number():
    return 42
print(get_number())
#Function calling another function:
def square(x):
    return x * x
def print_square(y):
    print("Square is:", square(y))
print_square(4)
#Recursive function (factorial):بحلها ع اللوب اولا حتى ما اضيع space
def factorial(n):
  if n == 0: #شرط التوقف كما في اللوب 
    return 1
  return n * factorial(n - 1)#تستدعي نفسها مرة اخرى
print(factorial(5))
print("*********************************")
# الحل عللى اللوب بالتال يبيكون افضل من حلها بالتكرار
res=1
n=5
while n>=1:
    res=res*n
    n=n-1
print(res)
print("*********************************")
for i in range(1,n+1):#بدانا من الواحد لانه هو اخر شي و+1 لان اخر قيمة ما هتفوت في الحل 
    res *=i
print(res)
print("*********************************")
def factorial(n):
    res=1
    for i in range(n,0,-1):#بدانا من الواحد لانه هو اخر شي و+1 لان اخر قيمة ما هتفوت في الحل 
        res *=i
    print(res)
# : Bubble Sort as a Function
def bubble_sort(arr):
 n = len(arr) # طول المصفوفة
 for i in range(n):
  for j in range(0, n - i - 1):
   if arr[j] > arr[j + 1]: 
    arr[j], arr[j + 1] = arr[j + 1], arr[j] # swap تبديل اماكنهم ليكون العنصر الاصغر قبل
numbers = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(numbers)
print("Sorted array:", numbers)
nums=[2,6,1,7,9,4,8]
print(nums)
for i in range(len(nums)):
   for j in range(i+1,len(nums)):
      if nums[j]<nums[i]:
         temp = nums[i]
         nums[i]=nums[j]
         nums[j]=temp
print(nums)
