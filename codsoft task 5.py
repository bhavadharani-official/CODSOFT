contacts = []

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    print("Contact added successfully.\n")

def view_contacts():
    if not contacts:
        print("No contacts found.\n")
        return
    print("\nContact List:")
    for i, c in enumerate(contacts,start=1):
        print(f"{i}. Name: {c['name']} | Phone: {c['phone']}")
        print()

def search_contact():
    query = input("Enter name or phone number to search: ").lower()
    found=False
    for c in contacts:
        if query in c["name"].lower() or query in c["phone"]:
            print(f"\nName: {c['name']}")
            print(f"Phone: {c['phone']}")
            print(f"Email: {c['email']}")
            print(f"Address: {c['address']}\n")
            found=True
            if not found:
                print("Contact not found.\n")

def update_contact():
    name=input("Enter the name of the contact to update: ").lower()
    for c in contacts:
        if c["name"].lower()==name:
            print("Leave input blank to keep current value.")
            c["name"]=input(f"New Name Current: {c['name']}): ") or c["name"]
            c["phone"]=input(f"New Phone(Current: {c['phone']}): ") or c["phone"]
            c["email"]=input(f"New Email(Current: {c['address']}): ") or c["address"]
            print("Contact updated successfully.\n")
            return
        print("Contact not found.\n")

def delete_contact():
    name= input("Enter the name of the contact to delete: ").lower()
    for i, c in enumerate(contacts):
        if c["name"].lower()==name:
            confirm=input(f"Are you sure you want to delete {c['name']}?(y/n): ")
            if confirm.lower()=='y':
                contacts.pop(i)
                print("Contact deleted successfully.\n")
            else:
                print("Deletion cancelled.\n")
                return
    print("Contact not found.\n")

def main():
    while True:
        print("Contact Book Menu")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print(" 4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")
        if choice=="1":
            add_contact()
        elif choice=="2":
            view_contacts()
        elif choice=="3":
            search_contact()
        elif choice=="4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice =="6":
            print("Existing Contact Book.Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")
main()
        
    
               
