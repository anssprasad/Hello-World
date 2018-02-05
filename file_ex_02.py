# This program prompts user to enter file name  then opens that file and reads through the file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.

fname = input("Enter fie name:")
fh = open(fname)
count = 0
total = 0
count_lines = 0
for line in fh :
    count_lines = count_lines + 1
    if not line.startswith('X-DSPAM-Confidence:') : continue
    else :
          pos = line.find(':')
          value = line[pos+1:]
          fvalue = float(value)
          total = total + fvalue
          count =  count + 1
average = total/count
print('Average Spam Confidence:',average)
print(total)
print(count)
print(count_lines)