
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


3.3 Simple Statistics with a List of Numbers
----------------------------------------------------

3.4 List Comprehensions
----------------------------------------------------

4.0 Working with Part of a List 
===================================================
	4.1 Slicing a List
    
    4.2 Looping through a slice
    
    4.3 Copying a List

5.0 Tuples
===================================================
	5.1 Definign a Tuple
    
    5.2 Looping Through All Values in a Tuple
    
    5.3 Writing over a Tuple
    
6.0 Styling Your Code
====================================================
	6.1 The Style guide
    
    6.2 Indentation
    
    6.3 Line Length
    
    6.4 Blank Lines
    
    6.5 Other Style Guidelines
