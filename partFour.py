savedUsername = "admin"
savedPassword = "password123"

print("Log in:")
username = input("Username: ")
password = input("Password: ")

while username != savedUsername and password != savedPassword:
    print("Wrong username or password.")
    print("")
    username = input("Username: ")
    password = input("Password: ")

print("Welcome '" + username + "'.")
