'''Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence
after sorting them alphabetically.
'''
inp = input("Enter words to be sorted ")
words = inp.split(",")
words.sort()
print (','.join(words))

