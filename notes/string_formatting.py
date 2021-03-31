score = 31
team = "Eagles"
isWinning = True

a = 15
b = 5

# f-Strings
# they are very similar to JS template literals
# you can have expressions in f-Strings

print(f"your score is {score}, your team is {team}, and your team winning is {isWinning}") # your score is 31, your team is Eagles, and your team winning is True
print(f"the total of {a} + {b} is: {a + b}") # the total of 15 + 5 is: 20

# str.format()
print("your score is {}, your team is {}, and your team winning is {}".format(score, team, isWinning)) # your score is 31, your team is Eagles, and your team winning is True

# string format operators (%)
# %s (string) 
# %d (decimal) 
# %f (float)
print("your score is %d, your team is %s, and your team winning is %s" % (score, team, isWinning)) # your score is 31, your team is Eagles, and your team winning is True
