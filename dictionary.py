data = {
    "name" : "talha",
    "phone" : "0300-0000000",
    "city" : "lahore",
    "age" : 20
}
# # print(data)
# # copy = data.copy()

# # print(data)
# # print(copy)

# # data["name"] = "ayan"
# # print(data)

# # del data["phone"]
# # print(data)

# # for key in data:
# #     print(key)
# #     for value in data.values():
# #         print(value)
# #         for key, value in data.items():
# #             print(f"{key}: {value}")

# # print(len(data))
# # print(data.keys())
# # print(data.values())
# # print("name" in data)

# student = [
#     {"name" : "adib", "marks" : 78},
#      {"name" : "rizwan", "marks" : 68},
#      {"name" : "sahil", "marks" : 65}   
# ]

# for students in student:
#     print(f"{students['name']} : {students['marks']}")

# practice

my_profile = {
    "name" : "talha kahn",
    "age" : 20,
    "city" : "ahemdabad",
    "hobby" : "coding",
    "language" : "python"
}

# print("=" * 35)
# print("       my_profile       ")
# print("=" * 35)

# for key, value in my_profile.items():
#     print(f"{key.upper():<12} : {value}")
#     print("=" * 35)
#     print(f"total info {len(my_profile)}")

my_profile.update(data)
print(my_profile)