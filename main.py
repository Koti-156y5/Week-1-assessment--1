from datetime import datetime

name = input("Enter your name: ")
print("Welcome", name)

while True:
    print("\n1. Study Tip")
    print("2. Motivation Quote")
    print("3. Current Date & Time")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        result = "Practice coding daily."
    elif choice == "2":
        result = "Success comes from consistency."
    elif choice == "3":
        result = str(datetime.now())
    elif choice == "4":
        break
    else:
        result = "Invalid Choice"

    print(result)

    with open("output.txt", "a") as file:
        file.write(result + "\n")