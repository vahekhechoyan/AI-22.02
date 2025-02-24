# 13
# Write a program that takes a sentence and splits it into words, then joins the words back into a sentence with hyphens (-) between them.
# Input: "I love Python"
# Output: "I-love-Python"

str="I love Python"
str1=str.split()
str2='-'.join(str1)
print(str2)