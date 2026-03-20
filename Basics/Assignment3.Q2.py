#  *** Deema Mohammed AL-Maqadma ***
# --->> Assignment 2: Prime Number Analyzer
# Let the user input a range of numbers.
# Use a function to check if a number is prime.
# Write all prime numbers in that range to a file, one per line.

def is_prime(x):
    if x<2 :
        return False
    for i in range(2,int(x**0.5)+1) : # ضفت 1 لتضمن العدد الصحيح الاخير
        if x%i == 0 :
            return False
    return True
print("**************************************\n")
def prime_analyzer():
    try:
        start = int(input("Enter the beginning :"))#لادخال بداية الارقام 
        end = int(input("Enter the last :"))
        primes=[str(num)for num in range(start,end+1)if is_prime(num)]#اضافة العنصر الاولي للقائمة
        with open("prime.txt","w") as f:
            f.write("\n".join(primes))
        print("The number of prime number :",len(primes))
    except ValueError:
        print("Error! Enter a valid value ...")
print("---->>> Welcome to the prime analuzor  <<<----\n")
prime_analyzer()
print("\n**************************************\n")
# حل اخر من احمد
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

start = int(input("Enter the beginning of the range: "))
end = int(input("Enter the end of the range: "))

file = open("prime_numbers.txt", 'w')

for number in range(start, end + 1):
    if is_prime(number):
        file.write(str(number) + '\n')

print("The prime numbers are saved in a file named: prime_numbers.txt.")
print("\n**************************************\n")

