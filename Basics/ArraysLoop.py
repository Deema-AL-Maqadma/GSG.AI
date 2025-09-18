
nums = [1, 2, 3]
names = ["Ali", "Sara"]
mixed = [42, "Hello", 3.14]
print(nums[0])#The value of item at index
nums[1] = 20 #modifying
print(nums) # print all items
for name in names: # loop at the value of item
    print("Hello", name)
print("****************************************")
arr = []
for i in range(3): #loop at the index of item
    arr.append(int(input("Enter number: "))) #insert at last
print(len(arr)) #length
arr.append(99)
print(arr)
arr.remove(99)
print(arr)
arr.sort() #sorting assending
print(arr)
print("Sara" in names) # لفحص وجود القيمة
print("****************************************")
for i in range(5): #طباعة رقم index من الصفر للرقم بين الاقواس-1
    print(i)
print("****************************************")
x = 0
while x < 5:
    print(x)
    x += 1
print("****************************************")
for i in range(1, 10, 2):
    print(i)
print("****************************************")
arr = [5, 3, 8]
for value in arr: # طباعة قيمة العنصر 
    print(value)
print("****************************************")
password = ""
while password != "1234":
    password = input("Enter password: ")
print("Access granted")
