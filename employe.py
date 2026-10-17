# employe salary details 
# fill the employe name 
print("-:Employe Name:-")
employe_name = input("Enter Employe Name :")
employe_age = int(input(f"{employe_name}-- please enter your age :"))
years_of_work = int(input(f"{employe_name}-- please enter your work expirans :"))

if years_of_work >= 10:
    print("your salary is 100000")
elif years_of_work >= 4:
    print("your salary is 40000")
elif years_of_work >= 2:
    print("your salary is 20000")
else:
    print("apply any other company")