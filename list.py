from ctypes.test import test_numbers
from test.test_builtin import StrSquares
bicycles=['trek','cannondale','redline','specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[1]+' '+'\n\t'+bicycles[3])
print(bicycles[-1])
message="My first bycyle was a "+bicycles[0].title()+", you bitches!"
print(message)

names=['nathaniel','victoria','emry','addison']
print(names[1])
message="I really want "
print(message+names[1].title()+" to slide my dick in her pussy")
print(message+names[2].title()+" to stop eating all the popsicles")
print(message+names[-1].title()+" to punch a cat in the face")
motorcycles=['honda','yahama','kawasaki']
print(motorcycles)
motorcycles[0]='ducati'
print(motorcycles)
motorcycles.append('honda')
print(motorcycles)
motorcycles.insert(1, 'mv')
print(motorcycles)
del motorcycles[2]
print(motorcycles)
removed_motorcycles=motorcycles.pop()
print(motorcycles)
print(removed_motorcycles)
print(motorcycles.pop())
last_owned=motorcycles.pop()
print("The last motorcycle I owned was a "+last_owned.upper()+" motorcyle!")
first_owned=motorcycles.pop(0)
print("The first motorcycle I owned was a "+first_owned.title()+" motorcycle!")
motorcycles=['honda','yahama','suzuki','ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)
motorcycles=['honda','yahamha','suzuki','ducati']
too_expensive='ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA "+too_expensive.title()+" is too expensive for my broke nigga ass")





cool_niggas=['trent reznor','maynard keenan','victoria johnson','your mom']
invite=", I would like to formally invite you to dinner and if you are lucky maybe some of dis DICK!"
print("\nDear "+cool_niggas[0].title()+invite)
print("Dear "+cool_niggas[1].title()+invite)
print("Dear "+cool_niggas[2].title()+invite)
print('Unfortunately '+cool_niggas.pop(-1).upper()+" has choked on a dick and can't make it")

cool_niggas.append('rob mason')

print("\nDear "+cool_niggas[-1].title()+invite)
print("\nWhat up peeps, your nigga found a bigger table")
cool_niggas.insert(0, 'arron dolly')
cool_niggas.insert(2, 'blake sheldon')
cool_niggas.append('cole vineyard')
print('\nDear '+cool_niggas[0].title()+invite)
print('Dear '+cool_niggas[2].title()+invite)
print('Dear '+cool_niggas[-1].title()+invite)

print('\nThis nigga fucked up and I can only invite two peeps')
cancel_invite=" sorry it looks like you gotta find some food some where else but don't worry you can always get some of the D"
print('\nWell '+cool_niggas.pop(0).title()+cancel_invite)
print('Well '+cool_niggas.pop(1).title()+cancel_invite)
print('Well '+cool_niggas.pop(1).title()+cancel_invite)
print('Well '+cool_niggas.pop(2).title()+cancel_invite)
print('Well '+cool_niggas.pop(-1).title()+cancel_invite)
print(cool_niggas)
del cool_niggas[0]
del cool_niggas[0]
print(cool_niggas)
whips=['bmw','audi','toyota','subaru']
whips.sort()
print('\n'+str(whips))
whips=['bmw','audi','toyota','subaru']
print("Here is the original list")
print(whips)
print("\nHere is the alphabetical list")
print(sorted(whips))
print("\nHere is the original list again")
print(whips)
whips.reverse()
print(whips)
print(len(whips))
witchs=['victoria','emry','addison','cathi']
for witch in witchs:
    print(witch.title())
for witch in witchs:
    print(witch.title()+", that was a super awesome trick!")
    print("I can't wait to see the next one,"+witch.title()+".\n")
for value in range(1,5):
    print(value)
numbers=list(range(1,6))
print(numbers)
even_numbers=list(range(2,11,2))
# The range values here are to go from 2 to 11 in increments of 2
print(even_numbers)
odd_numbers=list(range(1,11,2))
print(odd_numbers)
three_numbers=list(range(1,13,3))
# The range values here are to go from 1 to 13 in increments of 3
print(three_numbers)
squares=[]
for value in range(1,25):
    square=value**2
    squares.append(square)
print(squares)
##Now we write the same thing but even shorter
squares=[]
for value in range(1,25):
    squares.append(value**2)
print(squares)
print(min(squares))
print(max(squares))
print(sum(squares))
## Now even shorter code to populate the list of square numbers by doing all the work when we identify the list
squares=[value**2 for value in range(1,25)]
print(squares)
players=['charles','martina','michael','florence','eli']
print(players[0:3])
print(players[2:])
print(players[-3:])
print("Here are the first three players on my team: ")
for player in players[:3]:
    print(player.title())
first_three=[player for player in players[:3]]    
print("The first three players in my team are "+str(first_three).title()+".")

