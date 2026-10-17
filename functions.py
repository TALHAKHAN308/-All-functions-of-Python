# def greet(name):
#     print("=" * 30)
#     print(f"Hello {name}")
#     print("=" * 30)

# greet("Ali")

# def hello():
#     print("hello talha")

# hello()

# def greet(name):
#    print(f"kese ho {name}!..")

# greet("Talha")

# def add(a,b):
#     result = a + b
# return result
# print(add(10,50))

# def sum(a,b):
#     result = a / b, a + b, a - b
#     return result
# a = int(input("enter number a... "))
# b = int(input("enter number b... "))
# print(sum(a,b))

# def get_grade(marks):
#     if marks >= 80:
#         return "A"
#     elif marks >= 60:
#         return "B"
#     elif marks >= 40:
#         return "C"
#     else:
#         return "F(Fail)"
# marks = float(input("Enter Your Marks:- "))
# print(f"your grade is {get_grade(marks)}")

# def get_bmi(weight,height):
#     bmi = weight / (height * height)
#     return round(bmi,2)
# weight = float(input("Enter Your Weight:- "))
# height = float(input("Enter Your Height:- "))
# print(f"BMI:- {get_bmi(weight,height)}")

# def add_all(*args):
#     total = 0
#     for num in args:
#         total = total + num
#     return total
# print(add_all(2,4,67,31,6))

# def my_profile(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key.upper()}: {value}")

# my_profile(name = "talha",umar = 20,city = "ahemdabad")

def get_grade(marks):
    if marks >= 80:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 40:
        return "C"
    else:
        return "F"

def class_average(*marks):
    return sum(marks) / len(marks)

square = lambda x: x * x

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(get_grade(85))
print(class_average(85,92,78,65))
print(square(5))
print(f"5! = {factorial(5)}")


