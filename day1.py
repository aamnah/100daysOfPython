# 1000 Days of Python - Day 1

# print() - to output information to console
# input () - ask for user input in the console

# the print() will print the world "Hello" and the user input
print(input("Are you human? ") + ". ok!")

# name is a variable here. you don't need a `var` or `let` keyword like other languages (for example JS)
name = input("What's your name? ")
print("Hi " + name + "!")

interests =  input("What are your interests? ")

print(name + " likes " + interests + "!") # Aamnah likes coding

# print( name + " is " + len(name) + " characters long.") # TypeError: can only concatenate str (not "int") to str

age = 12

print(name + " who is " + str(age) + " year(s) old likes " + interests) # Amna who is 12 year(s) old likes coding

print(name + " who is " + age + "year(s) old likes " + interests) # TypeError: can only concatenate str (not "int") to str