__author__ = 'student'
contacts = {"jay": [1, 2, 3, 4], "bob": [2, 2, 2, 2]}
while True:
    userInput = raw_input("what do you like to do? ")

    if userInput == "view":
        viewContact = raw_input("Who do you like to view: ")
        if viewContact in contacts.keys():
            print contacts
        else:
            print viewContact + " not found!"

    elif userInput == "add":
        newContact = raw_input("Enter name: ")
        newPhone1 = raw_input("Enter primary phone: ")
        newPhone2 = raw_input("Enter secondary phone: ")
        newEmail = raw_input("Enter email: ")
        newAddress = raw_input("Enter address: ")

        confirm = raw_input("Are you sure you want to add this person? ")
        if confirm == "yes":
            contacts[newContact] = [newPhone1, newPhone2, newEmail, newAddress]
            print contacts

    elif userInput == "delete":
        deleteContact = raw_input("Enter Name of contact to be deleted: ")
        if deleteContact in contacts.keys():
                confirm = raw_input("Are you sure you want to delete this person? ")
                if confirm == "yes":
                    contacts.pop(deleteContact)
                    print contacts
        else:
            print "Contact not found!"

    elif userInput == "edit":
        editContact = raw_input("Enter contact to be edited: ")
        if editContact in contacts.keys():
                print ("press 1 for name")
                print ("press 2 for primary phone")
                print ("press 3 for secondary phone")
                print ("press 4 for email")
                print ("press 5 for address")
                editOptions = raw_input("What would you like to edit? ")
                if editOptions == "1":
                    editName = raw_input("Enter Name: ")
                    newEditName = contacts[editContact]
                    contacts[editName] = newEditName
                    del contacts[editContact]

                elif editOptions == "2":
                    editPhone1 = raw_input("Enter new Primary Phone Number: ")
                    contacts[editContact][0] = editPhone1

                elif editOptions == "3":
                    editPhone2 = raw_input("Enter  new Secondary Phone number: ")
                    contacts[editContact][1] = editPhone2

                elif editOptions == "4":
                    editEmail = raw_input("Enter new Email: ")
                    contacts[editContact][2] = editEmail

                elif editOptions == "5":
                    editAddress = raw_input("Enter new Address: ")
                    contacts[editContact][3] = editAddress

                print "Contact Updated"
                print contacts

        else:
            print("Contact not found!")

    elif userInput == "quit":
        break








