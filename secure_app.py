import subprocess

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "secure_input":
    print("Login successful")

command = input("Enter allowed command: ")

allowed_commands = ["ls", "pwd"]

if command in allowed_commands:
    subprocess.call([command])
else:
    print("Command not allowed")
