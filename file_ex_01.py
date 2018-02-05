#This program asks user to enter file name and convert all the words in the file to uppercase letters.
fname = input("Enter file name:")
fh= open(fname)
for line in fh :
    line = line.rstrip()
    line = line.upper()
    print(line)
