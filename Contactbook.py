def edit_contact():
    name_to_edit = input("Enter name for edit: ")

    try:
        with open("contacts.txt", "r") as file:
            lines = file.readlines()
        
        updated_lines = []
        found = False

        for line in lines:
            if name_to_edit.lower() in line.lower():
                print("Found: ", line.strip())
                new_name = input("Enter new name: ")
                new_phone = input("Enter new phone: ")
                updated_lines.append(f"{new_name},{new_phone}\n")
                found = True
            
            else:
                updated_lines.append(line)
        
        if found:
            with open("contacts.txt", "w") as file:
                file.writelines(updated_lines)
            print("Contact updated")

        else:
            print("Contact not found")

    except FileNotFoundError:
        print("The contacts file has not been created yet")

def delete_contact():
    name_to_delete = input("Enter name for delete: ")

    try:
        with open ("contacts.txt", "r") as file:
            lines = file.readlines()
        
        with open ("contacts.txt", "w") as file:
            deleted = False
            for line in lines:
                if name_to_delete.lower() not in line.lower():
                    file.write(line)

                else:
                    deleted = True
        
        if deleted:
            print("Contact is deleted")

        else:
            print("Contact isn't found")
    except FileNotFoundError:
        print("The contacts file has not been created yet.")



def find_contact():
    search_name = input("Enter name for find: ")

    try:
        with open("contacts.txt", "r") as file:
            found = False
            for line in file:
                if search_name.lower() in line.lower():
                    print("Found: ", line.strip())
                    found = True
            if not found:
                print("Contact isn't found")
    except FileNotFoundError:
        print("The contacts file has not been created yet.")

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter number: ")
    with open("contacts.txt", "a") as file:
        file.write(f"{name}: {phone}\n")
    print("Contact saved")

def show_contacts():
    try:
        with open("contacts.txt", "r") as file:
            contacts = file.readlines()
            print("List of contacts:")
            for contact in contacts:
                print(contact.strip()) 
    except FileNotFoundError:
        print("The contacts file has not been created yet.")

def main():
    while True:
        print("1. Add contact")
        print("2. Show all contacts")
        print("3. Find contact")
        print("4. Delete contact")
        print("5. Edit contact")
        print("6. Exit")
        choice = input("Choose action: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            show_contacts()
        elif choice == "3":
            find_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            edit_contact()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Wrong action")

main()