user =  input('please enter a word with 10 letters')
if len(user) == 10:
    print (user[0],user[-1])
    target = ""
    for letter in user:
        target += letter 
        print(target)
    
elif len(user) < 10:
    print('word not long enough')
else:
    print('word too long')

# word = 'helloworld'
target = ""
for letter in user:
    target += letter 
    print(target)
  


