import os

def view():
 
    try:
        with open("password.txt", "r") as file:
            lines = file.readlines()
            if not lines:
                print("No saved passwords.")
                return

            for line in lines:
                print(line.strip()) 
    except FileNotFoundError:
        print("No passwords saved yet.")

def add():
    

    if os.path.exists("password.txt"):
        with open("password.txt", "r") as file:
            lines = file.readlines()
    else:
        lines = []

    index = len(lines) // 2 + 1  

    user = input("What is the username or Email? ")
    password = input("What is your Password? ")
    platform = input("What platform or website? ")

    with open("password.txt", "a") as file:
        file.write(f"{index}. Username: {user} | Password: {password} | Platform: {platform}\n\n")
    
    print(f"Password saved as entry {index}!")

def delete():
    """Function to delete an entry by index"""
    try:
        with open("password.txt", "r") as file:
            lines = [line for line in file if line.strip()]  # Remove empty lines
        
        if not lines:
            print("No saved passwords to delete.")
            return
        
        # Display current passwords
        for line in lines:
            print(line.strip())

        index_to_delete = input("Enter the index number to delete: ")

        # Filter out the selected index
        new_lines = [line for line in lines if not line.startswith(f"{index_to_delete}.")]

        # Renumber remaining entries
        fixed_lines = []
        index = 1
        for line in new_lines:
            fixed_lines.append(f"{index}. " + line.split(". ", 1)[1])  # Fix index
            index += 1

        # Write updated list back to the file
        with open("password.txt", "w") as file:
            file.writelines(fixed_lines)

        print(f"Entry {index_to_delete} removed and indexes updated!")

    except FileNotFoundError:
        print("No saved passwords found.")

# Request main password
protection = input("Type your main password: ").lower()

while True:
    ask = input("What do you want to do (Add, View, Delete, q to exit)? ").lower()
    
    if ask == "q":
        print("Exiting the password manager.")
        break
    elif ask == "add":
        add()
    elif ask == "view":
        view()
    elif ask == "delete":
        delete()
    else:
        print("Invalid option. Please enter 'Add', 'View', 'Delete', or 'q'.")
