- [100 Days of Code - The Complete Python Pro Bootcamp for 2021](https://www.udemy.com/course/100-days-of-code/)
- [Repl.it](https://replit.com/@aamnah/100daysOfPython)

# Python Syntax Cheatsheet

| Description                    | Syntax                   | Example                      |
| ------------------------------ | ------------------------ | ---------------------------- |
| Variable                       | no `var` or `let` needed | `name = Aamnah`              |
| Assignment operator            | `=`                      | `age = 27`                   |
| Concatenation operator         | `+`                      | `"Hello " + name`            |
| Comments                       | `# comment`              |                              |
| Show stuff in the console      | `print()`                | print(`"Hello " + name`)     |
| Take user input in the console | `input()`                | input("What is your name? ") |
| Check the _type_ of data       | `type()`                 | `type(3.14)`                 |

## String formatting

```python
# f-Strings
print( f"the total of {a} + {b} is: {a + b}" )
print( f"{name} is {age}" )

# str.format()
print( "{} is {}".format(name, age) )

# string formatting operators
print( "%s is %d" % (name, age) )
```

## Math

```python
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
```
