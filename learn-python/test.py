from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    age: int
    salary: int
    dept: str

profile = {"name": "Hassan", "age": 27}
members = [{"name": "Hassan", "age": 27}, {"name": "Musa", "age": 16}]

# message = f"hi! I am {profile["name"]} and am {profile['age']}"

# print(message)

# memberFormat = [
#     {"label": member["name"], "value": member["age"]}
#     for member in members
#     if member["name"] is not "Hassan"
# ]

# print(memberFormat)

# for key, value in profile.items():
#     print(key, value)

# for key in profile.keys():
#     if key == "name":
#         profile["name"] = "Hassan Tahawar"
#         print(profile)
#     print(key)

# print(profile)

all_adults = all(member["age"] >= 18 for member in members)

print(all_adults)

hassan = Employee("Hassan", 27, 3000, "FE")

print(hassan.name)