
1.0 Looping through an Entire List
==================================================

	loop : the same action with every item in a list
`
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician)
`   
1.1 A Closer Look at Looping 
---------------------------------------------------	
`
for magician in magicians:
	print(f"{magician.title()}, that was a great trick!")
	printf(f"I can't wait to see your next trick, {magician.title()}.\n")
`
1.2 Doing More Work within a for Loop
----------------------------------------------------
	every indented line following the line for magician in magicians is considered inside loop
	
1.3 Doing Something after a for Loop
----------------------------------------------------
	 any lines of code after the for loop that are not indented are executed once without repetition

2.0 Avoiding Indentation Errors
===================================================
2.1 Forgetting to Indent
---------------------------------------------------
	always indent the line after the for statement
`for magician in magicians:
 print(magician)
`
2.2 Forgetting to Indent Additional Lines
---------------------------------------------------
`
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(f"{magician.title()}, that was a great trick!")
print(f"I can't wait to see your next trick, {magician.title()}.\n")
`
the final value associated with magician is carolina she is the only one who receives the looking forward to the next trick message

2.3 Indenting Unnecessarily
----------------------------------------------------
2.4 Indeting Unnecesarily After the Loop
----------------------------------------------------
2.5 Forgetting the Colon
----------------------------------------------------

3.0 Making Numerical Lists
===================================================
3.1 Using the range() Function
---------------------------------------------------
	range() function : start counting at the first value you give, and it stops when it reaches the second value you provide
` 
for value in range(1, 4+1):
	print(value)
`
`
range(6) : return numbers from 0~5
`
3.2 Using range() to Make a List of Numbers
----------------------------------------------------
	list() function: make a list of numbers, you can convert the results of range() directly into a list using the list() function / third argument: step size when generating numbers

`
even_numbers = list(range(2, 11, 2))
print(even_numbers)
`
`
squares = []
for value in range(1, 11):
	square = value ** 2
    squares.append(square)
    
print(squares)
`
3.3 Simple Statistics with a List of Numbers
----------------------------------------------------
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
min(digits)
max(digits)
sum(digits)

3.4 List Comprehensions
--------------------------------------------------
list comprehension : combines the for loop and the creation of new elements into one line 
and automatically appends each new element
`
squares = [ value**2 for value in range(1, 11)]
print(squares)
`
4.0 Working with Part of a List 
===================================================
slice : a specific group of items in a list


4.1 Slicing a List
---------------------------------------------------
to make a slice you specifiy the index of the first and last elements you want to work with

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

4.2 Looping through a slice
--------------------------------------------------- 
print("Here are the first three players on my team:")
for player in players[:3]:
	print(player.title())

4.3 Copying a List
---------------------------------------------------
my_foods = ['piza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

5.0 Tuples
tuple : an immutable list
===================================================
5.1 Defining a Tuple
--------------------------------------------------- dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

tuples are technically defined by the presence of a comma 
my_t = (3,)

5.2 Looping Through All Values in a Tuple
--------------------------------------------------- 
dimensions = (200, 50)
for dimension in dimensions:
	print(dimension)
    
5.3 Writing over a Tuple
--------------------------------------------------- 
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
	print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
	print(dimension)

6.0 Styling Your Code
====================================================
6.1 The Style guide
----------------------------------------------------    
6.2 Indentation
----------------------------------------------------     
6.3 Line Length
----------------------------------------------------     
6.4 Blank Lines
----------------------------------------------------     
6.5 Other Style Guidelines
---------------------------------------------------- 

