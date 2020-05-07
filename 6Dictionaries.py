
6.0 dictionaries    
dictionaries : connect pieces of related info

1.0 A Simple Dictionary 
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

2.0 Working with Dictionaries
a dictionary in python is a collection of key-value pairs
each key is connected to a value
can use a key to access the value associated with that key
a key's value can be a number, a string, a list, or even another dictionary

alien_0 = {'color': 'green'}
color - key
green - associated value  

2.1 Accessing Values in a Dictionary
alien_0 = {'color': 'green', 'points': 5}
new_points = alien_0['points']
print(f"You just earned {new_points} points!")

2.2 Adding New Key-Value Pairs
Dictionaries are dynamic structures - can add new key-value 
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

2.3 Starting with an Empty Dictionary

alien_0 = {}
alien_0['color'] = 'green'
alien_0['[points'] = 5
print(alien_0)

2.4 Modifying Values in a Dictionary

alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")
alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")

2.5 Removing Key-Value Pairs

del statement to completely remove a key-value pair 
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['poiints']
print(alien_0)


2.6 A Dictioanry of Similar Objects
favorite_languages = {
  'jen': 'python',
  'sarah': 'c',
  'edward': 'ruby',
  'phil': 'python',
}
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

2.7 Using get() to Access Values

alien_0 = {'color: 'green', 'speed': 'slow'}

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

3.0 Looping through a Dictionary  
user_0 = {
  'username': 'efermi',
  'first': 'enrico',
  'last': 'fermi',
}
for key, value in user_0.items():
  print(f"\nKey: {key}")
  print(f"Value: {value}")

3.1 Looping through All Key-Value Pairs
user_0 = {
  'username': 'efermi',
  'first': 'enrico',
  'last': 'fermi',
}

for key, value in user_0.items():
  print(f"\nKey: {key")
  print(f"Value: {value")

the method items() : returns a list of key-value 

favorite_languages = {
  'jen': 'python',
}
for name, language in favorite_languages.items():
  print(f"name.title()}'s favorite language is {language.title()}.")

3.2 Looping through all the Keys in a Dictionary  

the keys() method : useful when you dont't need to work with all of the values in a dictionary

for name in favorite_languages.keys():
  print(name.title())

3.3 Looping through a dictionary's keys in a particular order

for name in favorite_languages.key():
  print(name.title())

3.4 Looping through all values in a dictionary
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
  print(name.title())

  if name in friends:
    language = favorite_languages[name].title()
    print(f"\t{name.title()}, I see you love {language}!")

the method keys() : returns a list of all the keys 

3.5 Looping through a dictionary's keys in a particular order

for name in sorted(favorite_languages.keys()):
  print(f"{name.title()}, thank you for taking the poll.")

sorted() function : tells python to list all keys in the dictionary and sort that list before looping through it

3.6 Looping Through all values in a dictionary

print("The following langauges have been mentioned:")
for language in favorite_languages.values():
  print(language.title())

values() : return a list of values without any Keys

set : a collection in which each item must be unique
for language in set(favorite_language.values()):
  print(language.title())


4.0 Nesting

nesting: storing multiple dictionaries in a list / a list of items as a value in a dictionary

4.1 A List of Dictionaries




4.2 A List in a Dictionary




4.3 A Dictionary in a Dictionary






