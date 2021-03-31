### Notes

- `print()` to output info to the console
- `input()` to take user input inside console
- `print(input())` to take user input and show that input back. e.g. `print("Hello " + input("What is your name? "))`
- `+` is the concatenation operator. Concatenation is when you combine two strings. You can _only_ concatenate _strings_
- `\n` is for new line
- comments begin with `#`
- `len()` is the function for calculating string length. e.g `print(len("Aamnah"))`

### Conclusion

Learnt how to print stuff to the console, how to take a user's input, using built-in functions like `len()`, saving and using _variables_, and joining multiple strings to make a sentence (i.e. _concatenation_).

### Comments

```python
# this is a single line comment
print("hi there")
```

```python
print("hello") # comment can start at the end of the line as well
```

```python
# Since Python will ignore string literals that are not assigned to a variable,
# you can add a multiline string (triple quotes) in your code,
# and place your comment inside it:
```

Multi-line _strings_ start with _three quotes_. Either `'''` or `"""`. If you don't assign the string to anything then it can serve as a multi-line comment (hacky way of multiline comments really). The alternative is just adding `#` in the beginning of every line, works alright.

```
# Since Python will ignore string literals that are not assigned to a variable,
# you can add a multiline string (triple quotes) in your code,
# and place your comment inside it:
```

```python
"""
This text between three quotes will be treated as a comment
because we haven't really assigned it to anything,
it will be ignored
"""
```

### Variables

- No need for a `var` or `let` keyword. Just use `=` to assign a value.
- Variable names can not have spaces in them, they can't start with a number and they should not be any of the reserved keywords.. `my name`, `8ball`, and `print` are all bad/invalid variable names.

```python
name = "Aamnah"
age = 12

print(name + " is " + age "year(s) old.")
```

### Concatenation

If you want to combine multiple _strings_, you can use the `+` operator. It ONLY works for strings though, you can't do _Aamnah (string) is 12 (int) years old_..

```python
name = "Aamnah"
interests = "coding"
age = 12
```

```python
print(name + " likes " + interests) # Aamnah likes coding
```

You can't concatenate a `string` and an `int`

```python
print(name + " who is " + age + "year(s) old likes " + interests) # TypeError: can only concatenate str (not "int") to str
```

If you _cast_ (i.e. convert) the `int` as a `string` then it'll work

```python
print(name + " who is " + str(age) + "year(s) old likes " + interests) # TypeError: can only concatenate str (not "int") to str
```

### String formatting

Basically, you have 4 ways of getting string formatting.

- f-Strings (Python 3.6+)
- `str.format` (slightly newer style)
- `%` operator (old style, discourage but not deprecated. Very similar to `print-f` in _C_)
- Template strings (from Standard Library)

```python
name = "Aly"
age = 27

a = 15
b = 5

# f-Strings
print( f"the total of {a} + {b} is: {a + b}" )
print( f"{name} is {age}" )

# str.format()
print( "{} is {}".format(name, age) )

# string formatting operators
print( "%s is %d" % (name, age) )
```
