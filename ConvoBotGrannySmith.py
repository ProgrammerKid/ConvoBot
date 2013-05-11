import random
error = 'Sorry, I have not learned to understand what you just said, vboy36west@gmail.com'
version = '1.0.2 Granny Smith (Official Granny Smith)'

def worktodo():
    print 'Do your work'
    worktodo()





print version
print 'How are you doing'
feeling = raw_input()
if 'good' in feeling or 'okay' in feeling or 'perfect' in feeling or 'good' in feeling or 'fine' in feeling:
    print 'Nice to hear that'
elif 'bad' in feeling or 'horrible' in feeling or 'not very well' in feeling:
    print 'Sorry to hear that'
else:
    print error


meet = raw_input('Did you meet anyone new ')
if 'yes' in meet:
    print 'So what is there name'
    raw_input()
    print 'Okay, keep meeting new people, it is delicious.'
elif 'no' in meet:
    print 'Well try to meet new people, it is a good social skill'
else:
    print error



yn = raw_input('Ask me a yes or no question, and I will randomly answer it')
ran = round(random.random())
if ran == 0:
    print 'yes'
if ran == 1:
    print 'no'




money = raw_input('If I gave you a million dollars, what would you do with it')
if 'invest' in money or 'stock' in money:
    print 'That is very smart, most people do not think of that, but you are very smart'
else:
    print 'No, that is a very dumb thing to do, next time I ask you, give me a more educated answer'



todo = raw_input('Do you have work to do (type yes or no)').lower()
if todo == 'yes':
    print 'Then do your work'
    worktodo()
if todo == 'no':
    print 'Okay, good'

sib = raw_input('Do you have any sibling ')
if 'yes' in sib and 'brother' in sib:
    sibamount = raw_input('Brothers do you have? ').lower()
    if not '1' in sibamount and not 'one' in sibamount:
        broage = raw_input('Are they older or younger to you ').lower()
        if 'older' in broage:
            print 'Oh I have an older brother... you have really got to hate them'
        else:
            print 'I love younger brothers, even though I do not have one, but I am one'
    if '1' in sibamount or 'one' in sibamount:
        broage = raw_input('Is he older or younger to you ').lower()
        if 'older' in broage:
            print 'Oh I have an older brother... you have really got to hate them'
        else:
            print 'I love younger brothers, even though I do not have one, but I am one'
if 'yes' in sib and not 'bro' in sib:
    print 'okay'
    brosis = raw_input('Sister or brother').lower()
    if 'bro' in brosis or 'brother' in brosis:
        broage = raw_input('Older or younger ')
        if 'younger' in broage or 'young' in broage:
            print 'Younger brothers are really cool'
        elif 'older' in broage or 'old' in broage:
            print 'Older brothers suck'
if 'no' in sib:
    print 'Sucks, no one to talk to'
    lonely = raw_input('Do you ever feel lonely')
    if 'yes' in lonely or 'sometimes' in lonely:
        print 'mhhhm, at least you have me'
    elif 'no' in lonely or 'never' in lonely:
        print 'Oh, good... but even If you did feel lonely,,, you would always have me'
    else:
        print error

