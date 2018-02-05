fname = input('Enter file name:')
fh = open(fname)
lst = list()
for line in fh :
    line = line.rstrip()
    words = line.split()
    for i in list(range(len(words))) :
        found = 0
        for j in list(range(len(lst))) :
            if lst[j] == words[i] :
                found = 1
        if found == 0 :
            lst.append(words[i])

lst.sort()
print(lat)