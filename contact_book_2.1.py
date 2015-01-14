__author__ = 'student'
contacts = {"jay": [1, 2, 3, 4], "bob": [2, 2, 2, 2]} # dictionary where function will view, add, delete, and add
user_input = raw_input("what do you like to do? ")

"""
If the name is in the dictionary, it will print the contact info.
If not will print the "not found" then prompts global variable user_input.
"""
def view():
    if user_input == "view":
        view_contact = raw_input("Who do you like to view: ")
        if view_contact in contacts.keys(): # Searches name of the contact in contacts dictionary
            print contacts[view_contact]
        else:
            print view_contact + " not found!"

#Adds new contact info if user confirms "yes". If not, prompts global variable user_input
def add():
    if user_input == "add":
        new_contact = raw_input("Enter name: ")
        new_phone1 = raw_input("Enter primary phone: ")
        new_phone2 = raw_input("Enter secondary phone: ")
        new_email = raw_input("Enter email: ")
        new_address = raw_input("Enter address: ")

    confirm = raw_input("Are you sure you want to add this person? ")
    if confirm == "yes":
        # Adds new contact info the the cantacts dictionary
        contacts[new_contact] = [new_phone1, new_phone2, new_email, new_address]
        print contacts
"""
Prompts contact name to be deleted. It iterate contacts dictionary using name as key word.
If found and user confirms "yes". It deletes contact.
If user confirm "no", then prompts global variable user_input
If the name is not found, prints not found message then prompts global variable user_input
"""
def delete():
    if user_input == "delete":
        delete_contact = raw_input("Enter Name of contact to be deleted: ")
        if delete_contact in contacts.keys():
            confirm = raw_input("Are you sure you want to delete this person? ")
            if confirm == "yes":
                contacts.pop(delete_contact)
                print contacts
        else:
            print "Contact not found!"

def edit():
    if user_input == "edit":
        edit_contact = raw_input("Enter contact to be edited: ")
        """
        Searches name, which is the key for the dictionary contacts
        If name is in the contacts dictionary, prints following options
        """
        if edit_contact in contacts.keys():
                print ("press 1 for name")
                print ("press 2 for primary phone")
                print ("press 3 for secondary phone")
                print ("press 4 for email")
                print ("press 5 for address")
                edit_options = raw_input("What would you like to edit? ")
                if edit_options == "1": # Add new name then deletes new old name
                    edit_name = raw_input("Enter Name: ")
                    new_edit_name = contacts[edit_contact]
                    contacts[edit_name] = new_edit_name
                    del contacts[edit_contact]

                elif edit_options == "2":
                    edit_phone1 = raw_input("Enter new Primary Phone Number: ")
                    contacts[edit_contact][0] = edit_phone1 # Replaces old phone1 with new

                elif edit_options == "3":
                    edit_phone2 = raw_input("Enter  new Secondary Phone number: ")
                    contacts[edit_contact][1] = edit_phone2 # Replaces old phone2 with new

                elif edit_options == "4":
                    edit_email = raw_input("Enter new Email: ")
                    contacts[edit_contact][2] = edit_email # Replaces old email with new

                elif edit_options == "5":
                    edit_address = raw_input("Enter new Address: ")
                    contacts[edit_contact][3] = edit_address # Replaces old address with new

                print "Contact Updated"
                print contacts

# Executes the functions
while True:
    if user_input == "view":
        view()
        user_input = raw_input("what do you like to do? ")
    elif user_input == "add":
        add()
        user_input = raw_input("what do you like to do? ")
    elif user_input == "delete":
        delete()
        user_input = raw_input("what do you like to do? ")
    elif user_input == "edit":
        edit()
        user_input = raw_input("what do you like to do? ")
    elif user_input == "quit": # displays "Goodbye message then ends program
        print "Goodbye!"
        break







