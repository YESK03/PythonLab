import  re

data = input("Enter Email or Mobile Number")
email_pattern = r'[a-zA-z0-9. %+-]+@[a-zA-z0-9.-]+\.[a-zA-Z] {2,}$'
mobile_pattern = r'[0-9] {10}$'

if re.fullmatch(email_pattern, data):
    print("Valid Email ID")
    
elif re.fullmatch(mobile_pattern, data):
    print("Valid mobile Number")
    
else:
    print("Given value not valid")