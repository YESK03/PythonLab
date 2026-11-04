import pandas as pd

data = {
        
        "Name": ["Ram", "Bina", "Cristin", "Diana"],
        
        "Marks": [80, 90, 85, 70],
        
        "Phoneno": [8856839273,74847461988, 93274758320, 9336598800],
        
        "USN": ["01BCAR193", "01BCAR532", "01BCAR320", "01BCAR220"],
        
        "loc": ["UP", "HR", "BR", "OD"]
        
        
        
        
        
        
        
        
}

df = pd.DataFrame(data)
print(df)

print("Head \n", df.head())
print("Tail \n",df.tail())
print("Info \n",df.info())
print("Describe \n", df.describe())
print("Sorted",df.sort_values("Marks"))