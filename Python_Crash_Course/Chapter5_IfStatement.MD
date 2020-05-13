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
-----------------------------------------------------
	if conditional_test:
    	do something

	age = 19
    if age >= 18:
    	print("YOu are old enough to vote!")
        
3.2 if-else Statements
-----------------------------------------------------
if else : the else statement allows you to define an action or set of actions that are executed when the conditional test fails.

	age = 17
	if age >= 18:
    	print("You are old enough to vote!")
        print("Have you registered to vote yet?")
    else:
    	print("Sorry, you are too young to vote.")
        print("Please register to vote as soon turn 18!")

3.3 The if-elif-else Chain
------------------------------------------------------
	age = 12
    
    if age < 4:
    	print("Your admission cost is $0. ")
    elif age < 18:
    	print("Your admission cost is $25.")
    else:
    	print("Your admission cost is $40.")
        
Your admission cost is $25.

	age = 12
    
    if age < 4:
    	price = 0
    elif age < 18:
    	price = 25
    else:
    	price = 40
    
    print(f"Your admission cost is ${price}.")
    
3.4 Using Multiple elif Block
-------------------------------------------------------
	age = 12
    
    if age < 4:
    	price = 0
    elif age < 18:
    	price = 25
    elif age < 65:
    	price = 40
    else:
    	price = 20
    
    print(f"Your admission cost is ${price}.")
        
3.5 Omitting the else Block
------------------------------------------------------
	age = 12
    
    if age < 4:
    	price = 0
    elif age < 18:
    	price = 25
    elif age < 65:
    	price = 40
    elif age >= 65:
    	price = 20
    
    print(f"Your admission cost is ${price}.")

the else block : catchall statement, mathces any condition that wasn't matched by a specific if or elif test and can sometimes include invalid or even malicious data

3.6 Testing Multiple Conditions
------------------------------------------------------
use if-elif-else : if you want only oen block of code to run
use a series of independent if statements: if more than one block of code needs to run

- if-elif-else chain is appropriate to use when you jsut need one test to pass 


	requested_toppings = ['mushrooms', 'extra cheese']

	if 'mushrroms' in requested_toppings:
		print("adding mushrooms.")
	if 'pepperoni' in requested_toppings:
		print("Adding pepperoni.")
	if 'extra cheese' in requested_toppings:
		print('Adding extra cheese.")

	print("\nFinished making your pizza!")

Adding mushrooms.
Adding extra cheese.

Finished making your pizza!

	requested_toppings = ['mushrooms', 'extra cheese']
    
    if 'mushrooms' in requested_toppings:
    	print("Adding mushrooms.")
    elif 'pepperoni' in requested_toppings:
    	print("adding pepperoni.")
    elif 'extra cheese' in requested_toppings:
    	print("Adding extra cheese.")
        
    print("\nFinished making your pizza!")
    
    
Adding mushrooms.

Finished making your pizza!
4.0 Using if Statements with Lists
=====================================================
4.1 Checking for Special Items
------------------------------------------------------    

	requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
    
    for requested_topping in requested toppings:
    	print(f"Adding {requested_topping}.")
        
    print("\nFinished making your pizza!")
    
Adding mushrooms.
Adding green peppers.
Adding extra cheese.

Finished making your pizza!

	for requested_topping in requested_toppings:
    	if requested_topping == 'green peppers':
        	print("Sorry, we are out of green peppers right now.")
        else:
        	print(f"Adding {requested_topping}.")
            
        print("\nFinished making your pizza!")
 
 
4.2 Checking That a List is Not Empty
------------------------------------------------------    
	
    requested_toppings = []
    
    if requested_toppings:
    	for requested_topping in requested_toppings:
        	print(f"Adding {requested_topping}.")
        print("\nFinished making your pizza!")
    else:
    	print("Are you sure you want a plain pizza?")

4.3 Using Multiple Lists
------------------------------------------------------
	available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
    
    requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
    
    for requested_topping in requested_toppings:
    	if requested_topping in avilable_toppings:
        	print(f"Adding {requested_topping}.")
        else:
        	print(f"Sorry, we don't have {requested_topping}.")
            
    print("\nFinished making your pizza!")


5.0 Style Your if Statements
=====================================================
























