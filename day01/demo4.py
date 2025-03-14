# for
word = ['cat', 'dogq','window']
for w in word:
        print(w,len(w))

users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
for user, status in users.copy().items():
        if status == 'inactive':
                del users[user]
print(users)

active_users = {}
for user, status in users.items():
        if status == 'active':
                active_users[user] = status
print(active_users)