# 1 foot = 0.3048
# BMI = weight / height*height

height = input("enter your height in m: ")
weight = input("enter your height in kg: ")

height_float = float(height)
weight_float = float(weight)

bmi = weight_float / (height_float * height_float)

print(bmi) # 28.906249999999993
print(int(bmi)) # 28
print(round(bmi, 1)) # 28.9