import sys
print (sys.argv)

file1 = sys.argv[1]
file2 = sys.argv[2]
file3 = sys.argv[3]
#file1 = input('Enter first filename:')
#file2 = input('Enter second filename:')
#file3 = input('Enter third filename:')
fh1 = open(file1)
fh2 = open(file2)
fh3 = open(file3)
tot_tests = list()
testlist = list()
first = 0
def test_name(file_han) :
  testlist =list()
  for line in file_han  :
    line = line.rstrip()
    words = line.split(',')
  #print(words)
    if len(words)< 1 : continue
    else :
      testcode = words[0]
      if len(tot_tests)  == 0:
          tot_tests.append(testcode)
          testlist.append(testcode)
      else :

        found = 0
        repeated = 0
        for x in list(range(len(tot_tests))) :
            if tot_tests[x] == testcode :
                found = 1
        if found == 0 :
          tot_tests.append(testcode)
        if len(testlist) == 0 :
            testlist.append(testcode)
        else:
            for x in list(range(len(testlist))):
                if testlist[x] == testcode:
                    repeated = 1
            if repeated == 0:
               testlist.append(testcode)
  return(testlist)


#test_name(fh1)
test_list = list()
coded_list = list()
regres_list = list()
test_list = test_name(fh1)
#test_name(fh2)
coded_list = test_name(fh2)
#test_name(fh3)
regres_list = test_name(fh3)
print(tot_tests)
print(test_list)
print(coded_list)
print(regres_list)
fh4 = open("test_status.csv","w")
#for word in tot_tests :
#    fh4.write(word)
#    fh4.write('\n')
def compare(lst1,lst2,lst3) :
  for i in list(range(len(tot_tests))) :
    match = 0
    fh4.write(tot_tests[i])
    for j in list(range(len(lst1))) :
        if lst1[j] == tot_tests[i] :
            match = 1
    fh4.write(',')
    if match == 0 :
        fh4.write('False')
    else : fh4.write('True')
    match = 0
    for k in list(range(len(lst2))) :
        if lst2[k] == tot_tests[i] :
            match = 1
    fh4.write(',')
    if match == 0 :
        fh4.write('False')
    else : fh4.write('True')
    match = 0
    for l in list(range(len(lst3))) :
        if lst3[l] == tot_tests[i] :
            match = 1
    fh4.write(',')
    if match == 0 :
        fh4.write('False')
    else : fh4.write('True')
    fh4.write('\n')
compare(test_list,coded_list,regres_list)
#compare(coded_list)
#compare(regres_list)

fh4.close()

