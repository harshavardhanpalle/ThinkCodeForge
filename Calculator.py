# Simple Intreset Calculator
#SI = P T R / 100

P = float(input("Enter the actual Amount (P) : "))
T = float(input("Enter the Time Period (T): "))
R = float(input("Enter the Rate Of Intrest (R) : "))
# simple Intrest
SI = (P * T * R )/100

print(f"Simple Intrest Rate : {SI:.2f}" )




#Calculator
#add sub div mod mul 
a = float(input("enter first  number :"))
b = float (input("enter second number :"))

add = a + b  
sub = a - b
mul = a * b
div = a / b
mod = a % b # gives remainder

print("Addition of numbers :",add)
print("Subtraction", sub)
print("Multiplication",mul)
print("Division",div)
print("Modulus" , mod)



