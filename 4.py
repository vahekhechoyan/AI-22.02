# 4

#  Create Complex Numbers and Calculate Magnitude
# Create two fractions and perform addition, subtraction, multiplication, and division manually. Afterward, check the results using Python.
# Create a decimal number and experiment with adding or subtracting very small decimal values

from fractions import Fraction
from decimal import Decimal

complex_a=9+6j
complex_b=10+8j
print ("Complex number:", complex_a ,"Magnitut:",abs(complex_a))
print ("Complex number:", complex_b ,"Magnitut:",abs(complex_b))
 
a=Fraction(5,8)
b=Fraction(8,9)
add_fraction=a+b
div_fraction=a/b
mul_fraction=a*b
sub_fraction=a-b
print("a+b:",add_fraction) 
print("a/b:",div_fraction)
print("a*b:",mul_fraction)
print("a-b:",sub_fraction)

x=Decimal('0.55')
y=Decimal('0.0055')

print("x+y:",x+y)
print("x-y:",x-y)