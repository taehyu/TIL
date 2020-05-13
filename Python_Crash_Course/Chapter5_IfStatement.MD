1.0 A Simple Example
=====================================================
	cars = ['audi', 'bmw', 'subaru', 'toyota']

	for car in cars:
	if cars == 'bmw':
    	print(car.upper())
    else:
    	print(car.title())

2.0 Condtional Tests
=====================================================
conditional test : true or false

2.1 Checking for Equality
-----------------------------------------------------
	cars = 'bmw'
	cars == 'bmw'
	True

(==) double equal sign : equality operator

2.2 Ignoring Case when Checking for Eqaulity
-----------------------------------------------------
	car = 'Audi'
	car.lower() == 'audi'

lower() function: doesnt change the value that was originally stored in original car

Testing for equality is case sensitive

2.3 Checking for Inequality
-----------------------------------------------------
(!=) not : determine whether two values are not equal
`
requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
	print("Hold the anchovies!")
`

2.4 Numerical Comparisons
-----------------------------------------------------
	
	age = 18
	
	age == 18

	True


2.5 Checking Multiple Conditions     
-----------------------------------------------------
2.5.1. Using and to Check Multiple Conditions
	
	age_0 = 22
	age_1 = 18
	age_0 >= 21 and age_1 >= 21
	False

	age_1 = 22
	age_0 >= 21 and age_1 >= 21
	True

	(age_0 >= 21) and (age_1 >= 21)


2.5.2. Using or to Check Multiple Conditions

	age_0 = 22
	age_1 = 18
	age_0 >= 21 or age_1 >= 21
	True

	age_0 = 18
	age_0 >= 21 or age_1 >= 21
	False 

2.6 Checking Whether a Value is in a List    
-----------------------------------------------------
the key word "in" : to find out whether a particular value is already in a list 

	requested_toppings = ['mushrooms', 'onions', 'pineapple']

	mushrooms' in requested_toppings
	True

2.7 Checking Whetehr a Value is Not in a List   
-----------------------------------------------------
	banned_uers = ['andrew', 'carolina', 'david']
    user = 'marie'
	
    if user not in banned_users:
    	print(f"{user.title()}, you can post a response if you wish.")
Marie, you can post a response if you wish

2.8 Boolean Expressions
-----------------------------------------------------
- A Boolean value is either True or False
- Boolean values are often used to keep track of certain conditions, such as whether a game is runnign or whether a user can edit certain content on a website


	game_active = True
    can_edit = False

3.0 if Statements
=====================================================

	3.1 Simple if Statements
    
    3.2 if-else Statements
    
    3.3 The if-elife-else Chain
    
    3.4 Using Multiple elif Blocks
    
    3.5 Omitting the else Block
    
    3.6 Testing Multiple Conditions
    
4.0 Using if Statements with Lists
=====================================================

	4.1 Checking for Special Items
    
    4.2 Checking That a List is Not Empty
    
    4.3 Using Multiple Lists
    
5.0 Style Your if Statements
=====================================================