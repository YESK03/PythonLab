employee = {
    "Name": "Shuvam",
    "Age": 19,
    "Post": "Software Developer",
    "Salary": 200000
    
    }


print("Keys")
print(employee.keys())

print("Values")
print(employee.values())

print("Items:")
print(employee.items())

#get
print("Names:",employee.get("Name"))
print("Marks",employee.get("marks","Not Available"))


employee.update({"Age":18, "Marks":9})


print("After Updating")
print(employee)


