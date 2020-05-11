1.0 What really happens when you run hello_world.py

2.0 Variables

message = "hello world"
print(message)

	2.1 Naming and Using Variables
- Variable Names can contain only letters, numbers, underscores
can start with a letter, an underscore but not with a number
- spaces not allowed
- should be short but descriptive
- lowercase letter l,O often confused with the number 1, 0
the end

	2.2 Avoiding Name Errors when Using Variables
traceback: a record of where the interpreter ran into trouble when trying to execute your code.

	2.3 Variables are labels
-think of variables as labels that you can assign to values / variable references a certain value

3.0 Strings
'This is a string.'
"This is also a string."

	3.1 Changing Case in a String with Methods
a method : is an action that python can perform on a piece of data
name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

	3.2 Using Variables in Strings
f-strings : python formats the string by replacing the name of any variable in braces with its value
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")

	3.3 Adding Whitespace to Strings with Tabs or Newlines
whitespace: nonprinting character ex) spaces, tabs, end-of-line symbols
\n \t

	3.4 Stripping Whitespace

	3.5 Avoiding Syntax Errors with sTrings

4.0 Numbers

	4.1 Integers

	4.2 Floats 

	4.3 Integers and Floats

	4.4 Underscores in Numbers

	4.5 Multiple Assignment

	4.6 Constants

5.0 Comments

	5.1 How do you write comments?

	5.2 What Kind of Comments Should You Write?
