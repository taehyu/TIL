
1.0 What is a List

list: a collecttion of items in a particular order

bicycles = ['trek', 'cannondale']
print(bicycles)
['trek', 'cannondale']
	
    1.1 Accessing Elements in a List
index: the position of any element in a list
print(bicycles[0])
trek

	1.2 Index Positions Start at 0, Not 1
the first item in a list to be at position 0
the last element in a list / bicycles[-1]

	1.3 Using Individual Values from a List
message = f"My first bicycle was a {bicycles[0].title()}."

2.0 Changing, Adding and Removing Elements
most lists you create will be dynamic 

	2.1 Modifying Elements in a List
motorcycles[0] = 'ducati'

	2.2 Adding Elements to a List
	2.2.1. Appending Elements to the End of a List
motorcycles.append('ducati')
>>> bicycles = ['trek', 'cannondale', 'ducati']
motorcycles = [] / to use an empty list 
	
    2.2.2. Inserting Elements into a List
motorcycles.insert(0, 'ducati')
>>> ['ducati', 'honda', 'yamaha', 'suzuki']
    
	2.3 Removing Elemetns from a List
	2.3.1. Removing an Item Using the del Statement
del motorcycles[0]
    
    2.3.2 Removing an Item Using the pop() Method 
pop() method : removes the last item in a list, but lets you work with that item after removing 

    2.3.3. Popping Items from any Position in a List
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")
   
	2.3.4. Removing an Item by Value
remove() method: remove using the value of the item, not index
motorcycles.remove('ducati')

3.0 Organizing a List

	3.1 Sorting a List Permanently with the sort() Method
sort() method: sort alphabetically
cars.sort(reverse=True)

	3.2 Sorting a List Tempporarily with the sorted() Function
sorted() function
print(sorted(cars))
print(sorted(reverse=True)

	3.3 Printing a List in Reverse Order
reverse() method
cars.reverse()

	3.4 Finding a List in Reverse Order
len() function: length of a list
len(cars)

4.0 Avoiding Index Errors when Working with Lists
