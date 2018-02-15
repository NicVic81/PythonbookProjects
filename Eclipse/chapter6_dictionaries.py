alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
alien_0['x_position']=0
alien_0['y_position']=25
print(alien_0)
alien_0 = {'color':'green'}
print("The alien is "+alien_0['color']+'.')

alien_0['color']='yellow'
print('\nThe alien is now '+alien_0['color']+'.')

alien_0 = {'x_position':0,'y_position':25,'speed':'medium'}
print("The original x position is "+str(alien_0['x_position'])+'.')
#Move the alien to the right
#Determine how far to move the alien based on it's current speed
if alien_0['speed']== 'slow':
    x_increment = 1
elif alien_0['speed']== 'medium':
    x_increment = 2
else:
    #This must be one fast fucker
    x_increment = 3

# The new position is the old position plus the x_increment
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("The new x position is "+str(alien_0['x_position'])+".")

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi'
    }
# since there are keys and vaules we need to define to variables for the loop 
# and .items after the dictionary
for key, value in user_0.items():
    print('\nKey: '+ key.title())
    print('Value: '+ value.title())

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
for name, lang in favorite_languages.items():
    print(name.title()+"'s favorite programming language is "+lang.title()+".")
# You can use .key() if you just need the keys in a dictionary
for name in favorite_languages.keys():
    print(name.title()+' is a little bitch!')
    
friends = ['phil','sarah']
# just making a new list, could be having the user input his friends 
for name in favorite_languages.keys():
    #setting the varibale name with the key values from our dictionary
    print(name.title())
    
    if name in friends:
        #just a normal if else statement looking in the friends list
        print(" Hi "+name.title()+ ", I see your favorite programming language is "+
              favorite_languages[name].title()+"!")
        
if 'erin' not in favorite_languages.keys():
    print('\nErin, please take our poll (in the ass).')

for name in sorted(favorite_languages.keys()):
    print(name.title()+", thank you for taking our survey.")
    
print("The following languages have been mentioned: ")
for language in favorite_languages.values():
    print(language.title())
#here the set function makes sure to leave out repeats    
print("The following languages have been mentioned: ")
for language in set(favorite_languages.values()):
    print(language.title())
    
rivers_countries = {
    'nile2':'egypt',
    'nile':'egypt',
    'ohio':'america',
    'super wet':'your mom'
    }
for river, place in rivers_countries.items():
    print("The "+river.title()+' river is in '+place.title()+'.')

for river in sorted(set(rivers_countries.keys())):
    print(river.title())
#you should never have to sort the keys since they should be unique 
for place in sorted(set(rivers_countries.values())):
    print(place.title())
canidates=['victoria','emry','jen','nate','sarah','addison']
for person in sorted(canidates):
    if person in favorite_languages.keys():
        print("Thanks, "+person.title()+" for taking our poll.")
    else:
        print(person.title()+", please take our poll.")
        
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)
# Make an empty list for storing aliens 
aliens = []

# Make 30 green aliens 
for alien_number in range(30):
    new_alien = {'color': 'green','points':5, 'speed':'slow'}
    aliens.append(new_alien)
# now we are looping through the first three and if they are green then we change
# them to yellow and update the speed and points
for alien in aliens[:3]:
    if alien['color']== 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10    
# And now if they are yellow then they become red and faster
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
# Show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")
# Show how many aliens have been added to the list
print("Total number of aliens is "+str(len(aliens))+".")
# Store information about a pizza being ordered
pizza = {
    'crust' : 'thick',
    'toppings' : ['mushrooms','extra cheese']
    }
# Summarize the order
print("You ordered a "+pizza['crust']+"-crust pizza with the following toppings:")
for topping in pizza['toppings']:
    print("\t"+topping)

favorite_languages = {
    'nic' : [],
    'jen' : ['python','ruby'],
    'sarah' : ['c'],
    'edward' : ['ruby','go'],
    'dick' : ['python','haskell'],
    }
# I added the set and soted command to weed out duplicates and put in 
# Alphabetical order
for name, languages in sorted(favorite_languages.items()):
#adding if statements to refine the print statements
    if len(languages)<1:
        print("\n"+name.title()+" should take our survey!")
    elif len(languages)<2:
        print("\n"+name.title()+"'s favorite language is ")
        for language in languages:
            print("\t"+language.title())
    else:
        print("\n"+name.title()+"'s favorite languages are: ")
        for language in sorted(set(languages)):
            print("\t"+language.title())
            
users = {
    'aeinstein' : {
        'first' : 'albert',
        'last' : 'einstein',
        'location' : 'princeton',
        },
    'mcurie' : {
        'first' : 'marie',
        'last' : 'curie',
        'location' : 'paris',
        },
    }

for username, user_info in sorted(users.items()):
    print("\nUsername: "+username)
    full_name = user_info['first']+" "+user_info['last']
    location = user_info['location']
    
    print("\tFull name: "+ full_name.title())
    print("\tLocation: "+ location.title())
        
        