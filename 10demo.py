# 10demo.py by Veda Nayak

print("hello, again") # a nice greeting
 
''' 
This is a multiline comment
just for fun
'''

# MATH

print("Math operators")

print(1.5e-2) # 1.5 times 10 to the power of -2, so smart
print( 1 + 1 )
print( 1 - 1 )
print( 2 * 2)
print( 1 / 2 )
print( 2 ** 3 )
print( 5 // 2) # integer divide , truncates off the fraction output = 2
print( 5 % 2 ) # remainder
print ( 5 * (2 + 1) ) # PEMDAS

print("Math functions")

x = -5
y = 17

print(abs(x)) # absolute value of x
print(pow(x, y)) # x to the power of y
print(round(x, ndigits = 3)) # round off x to 3 digits

print("More math functions")
import math

x = 0.5
y = 2
n = 3

print(math.ceil(x)) # round x up
print(math.floor(x)) # round x down
print(math.log(x)) # x in log base e
print(math.log2(x)) # x in log base 2
print(math.log10(x)) # x in log base 10
print(math.sqrt(x)) # square root of x
print(math.pow(x,y)) # x to the power of y
print(math.factorial(n)) # factorial of integer n

print("Math library constants")
print(math.e)
print(math.pi)
print(math.inf) # infinity

# Variables
print("Assignment")
a = 3 
b = 4
c = math.sqrt(a**2 + b**2)
print(c)

print(type(a), type(b), type(c))

## The \n means whatever is after this gets printed on a new line
print(type(a), type(b), type(c), sep = ", ", end = "!\n")

def pythagoras(a, b): 
    c = math.sqrt(a**2 + b**2)
    print("The hypotenuse is", c)
    return c

pythagoras(3, 4)

# STRINGS
print("STRING")


# SORTING
print("SORTING")

print(ord('A'))
print(ord('7'))
print(ord(','))
print(ord('>'))

print(10 ** -3.2)
print(10 ** -2.2)
print(10 ** -1.1)

# 65 - 33 = 32 --> 10 ** -3.2
# 55 - 33 = 22 --> 10 ** -2.2
# 44 - 33 = 11 --> 10 ** -1.1
