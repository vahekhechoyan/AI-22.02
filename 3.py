# 3

# Create and Compare Numbers of Different Types
# Compare an integer and a float
# Compare a decimal and a float
# Compare two fractions

from decimal import Decimal
from fractions import Fraction
x=int(input("enter a number:"))
y=float(input("enter a number:"))
z=Decimal(input("enter a number:"))
a=Fraction(1,2)
b=Fraction(5,10)
print(f" {int}=={float}:", x==y)
print(f"{Decimal}=={float}:" , z==y)
print(f"{Fraction}=={Fraction}:", a==b)