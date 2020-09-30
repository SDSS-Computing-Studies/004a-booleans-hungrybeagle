#! python3

#  Have the user enter a username 
# If the username is not "admin" then tell them it is an "invalid user", 
# but if it is, then ask them for a password 
# If they get the password correct (password is 12345password) 
# then display the message "Access granted"
# 1 marks

name = input("Enter name:")
print(name)
if name == "admin":
    pw = input("Enter password:")
    if pw == "12345password":
        print("Access granted")
    else:
        print("Access denied")

else:
    print("invalid user")