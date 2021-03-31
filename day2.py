# 1000 Days of Python - Day 2
# Data Types

print("Hello"[1]) # e
print("123" + "456") # 123456
print(123 + 456) # 579

print(123_456_789)

# Type checking with type()
print(type("Hello")) # <class 'str'>
print(type(123)) # <class 'int'>
print(type(123_000_000)) # <class 'int'>
print(type(13.4)) # <class 'float'>
print(type(True)) # <class 'bool'>

# Type casting
myNumber = 123
print(type(str(myNumber))) # <class 'str'>
print(type(float(myNumber))) # <class 'float'>

myString = "567"
print(myNumber + float(myString)) # 690.0

# Math
print(3 + 5) # 8 -add
print(9 - 4) # 5 - subtract
print(3 * 9) # 27 - multiply
print(7 / 2) # 3.5 - divide (returns a float)
print(7 // 2) # 3 - floor (returns an int)
print(13 % 5) # 3 - modulus (remainder after division)
print(2 ** 3) # 8 - exponent
print(2 ** 3 ** 2) # 512 - exponent

#P-E-MD-AS (Left to Right)
print( 3 + 3 - 3 / 3 * 3 ) # 3.0
