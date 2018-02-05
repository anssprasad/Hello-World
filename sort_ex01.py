friends = ['Sam','Joseph','Alex']
new_friends = ['Sally','Joseph','Jack']


for i in list(range(len(friends))) :
        found = 0
        for j in list(range(len(new_friends))) :
            if new_friends[j] == friends[i] :
                found = 1
        if found == 0 :
            new_friends.append(friends[i])


print(new_friends)