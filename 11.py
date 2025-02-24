# 11
# Write a program that checks whether a string starts with the letter "A" and ends with the letter "Z".
# Input: "AmazingZ"
# Output: Starts with A: True, Ends with Z: True

str="AmazingZ"
start=str.startswith('A')
ends=str.endswith('Z')
print(start,ends)