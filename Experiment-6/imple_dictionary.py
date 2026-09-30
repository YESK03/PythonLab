employee = {
    "Name": "Shuvam",
    "Age": 19,
    "Post": "Software Developer",
    "Salary": 200000
    
    }


#add an element
employee["ID"] = "25BCAR0637"

print("After adding",employee)


#updating an element
employee["Age"] = 18

print("After Updating",employee)

#Deleting an element
del employee["Salary"]

print("After Deleting",employee)
