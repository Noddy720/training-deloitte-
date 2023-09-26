
// question no.1
from datetime import date
def test(month, year): 
    return str(date(year,month,13).strftime("%A")=='Monday')

month = 11;
year = 2022;            
print("Month No.: ", month, " Year: ", year);
print("Check whether the said month and year contains a Monday 13th.: " + test(month, year));
month = 6;
year = 2022;            
print("\nMonth No.: ", month, " Year: ", year);
print("Check whether the said month and year contains a Monday 13th.: " + test(month, year)); 

3.3

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = 10


if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))

3.1

def DecimalToOctal(n):
    # array to store octal number
    octal = [0] * 100

    
    i = 0

    # run until n is 0
    while (n != 0):
        # Storing Remainder in Octal Array
        octal[i] = n % 8
        # updating value of n to n/8
        n = int(n / 8)
        # Increasing the Counter
        i += 1
 
   
    for j in range(i - 1, -1, -1):
        print(octal[j], end="")

3.2
num = 1234
reversed_num = 0

while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

print("Reversed Number: " + str(reversed_num))

3.4
def fib(n, lookup):
 
    if n <= 1:
        return n
 
    if n not in lookup:
        lookup[n] = fib(n - 1, lookup) + fib(n - 2, lookup)
 
    return lookup[n]
 
 
if __name__ == '__main__':

2.

 
    n = 8
    lookup = {}
 
    print('F(n) =', fib(n, lookup))
