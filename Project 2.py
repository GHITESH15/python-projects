#Password Guessing
password="GPH"
user_password=input("Enter your password:")
while password!=user_password:
    print("Incorrect password")
    user_password = input("Enter your password:")

print("Access Granted")

