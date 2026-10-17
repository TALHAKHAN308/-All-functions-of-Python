name = input("Enter Your Name : ")
age = int(input("Enter Your Age :"))

print(f"Hello,{name} Nice to meet you.")
print(f"You are {age} years old.")

# age category
if  age > 12:
    print("You are chaild.")
elif age > 18:
    print("You are adult.")
elif age > 30:
    print("You are young.")
else:
    print("you are senior.")

# intersting facts
print(f"After 10 year your age is {age + 10}")
print(f"After 12 month your age is {age * 12}")
print(f"After 365 days you age is {age * 365}")

