#(해답)
for value in [3,2,1,0]:
    print(value)


#(해답)
guess_me=7
number=1

while True:
    if number < guess_me:
        print('too low')
    elif number == guess_me:
        print('found it!')
        break
    elif number > guess_me:
        print('oops')
        break
    number += 1


#(해답)
guess_me=5
for number in range(10):
    if number < guess_me:
        print("too low")
    elif number == guess_me:
        print('found it!')
        break
    else:
        print('oops')
        break
