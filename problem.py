#Student report card
# print name 
name = input("Enter student name : ")
print(name.upper())
print("\nEnter Student marks:-")

# enter marks 
math = float(input("math marks (out of 100):-"))
english = float(input("english marks(out of 100):-"))
sience = float(input("sience marks (out of 100):-"))

total = math + english + sience
average = total / 3
percentage = (total/300) * 100

print(f"\n===== {name}'s report card =====")
print(f" math:     {math}")
print(f" english:  {english} ")
print(f" sience:   {sience}")
print(f"--------------------------------------------")
print(f"total:     {total}/300")
print(f"average:   {average:.2f}")
print(f"percentage:{percentage:.2f}%")

if percentage >= 80:
    print("Grade : A -  pass")
elif percentage >= 60:
    print("Grade : B -  pass")
elif percentage >= 40:
    print("Grade : C -  pass")
else:
    print("Grade : F -  fail")
