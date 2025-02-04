song="""When an eel grabs your arm,
And it causes great harm,
That's - a moray!"""

#(오답) song.title()
#(해답)
song=song.replace(" m", " M")
print(song)

# 문자열 일부를 대체하기 위해서는 replace() 사용
# " m"을 " M"으로 대체 (m으로 시작하는 단어를 대문자로 만들어야 하므로 공백 포함하여 대체 필요)


#(오답)
#q1={"We don't serve string around here. Are you a string?":"An exploding sheep."}
#q2={"What is said on Father's Day in the forest?":"No, I'm a frayed knot."}
#q3={"What makes the sound 'Sis! Boom! Bah!'?":"'Pop!' goes the weasel."}

#print(q1)
#print(q2)
#print(q3)

#(해답)
questions=[
    "We don't serve string around here. Are you a string?",
    "What is said on Father's Day in the forest?",
    "What makes the sound 'Sis! Boom! Bah!'?"
]
answers=[
    "An exploding sheep.",
    "No, I'm a frayed knot.",
    "'Pop!' goes the weasel."
]
q_a=((0,1), (1,2), (2,0))
for q, a in q_a:
    print("Q:", questions[q])
    print("A:", answers[a])
    print()


cat="My kitty cat likes %s, My kitty cat likes %s, My kitty cat fell on his %s And now thinks he's a %s." % ('roast beef', 'ham', 'head', 'clam')
print(cat) 

#(해답)
poem='''
My kitty cat likes %s, 
My kitty cat likes %s, 
My kitty cat fell on his %s 
And now thinks he's a %s.'''

args=('roast beef', 'ham', 'head', 'clam')
print(poem%args)


letter="""Dear {salutation} {name},
Thank you for your letter. We are sorry that our {product} {verbed} in your room.
Please note that it should never be used in a {room}, especially near any {animals}.
Send us your receipt and {amount} for shipping and handling. 
We will send you another {product} that, in our tests, is {percent}% less likely to have {verbed}.
Thank you for your support.
Sincerely,
{spokesman}
{job_title}"""

#(해답)
print(letter.format(salutation='Ambassador',
                    name='Nibbler',
                    product='pudding',
                    verbed='evaporated',
                    room='gazebo',
                    animals='octothorpes',
                    amount='$1.99',
                    percent=88,
                    spokesman='Shirley Iugeste',
                    job_title='I Hate This Job'))


#(해답)
names=["duck", "gourd", "spitz"]
for name in names:
    cap_name=name.capitalize()
    print("%sy Mc%sface" % (cap_name, cap_name))

for name in names:
    cap_name=name.capitalize()
    print("{}y Mc{}face".format(cap_name, cap_name))

for name in names:
    cap_name=name.capitalize()
    print(f"{cap_name}y Mc{cap_name}face")
