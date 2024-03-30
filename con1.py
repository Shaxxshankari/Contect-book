class ContMang:
    def __init__(self):
        self.cont = {}

    def add_cont(self, name, phone_no, email, addr):
        self.cont[name] = {
            'ph_no': phone_no,
            'email': email,
            'addr': addr
        }
        print("Contact added successfully.")

    def view_cont(self):
        if self.cont:
            print("Contact List:")
            for name, info in self.cont.items():
                print(f"Name: {name}, Phone Number: {info['ph_no']}")
        else:
            print("Contact list is empty.")

    def srch_cont(self, query):
        res = []
        for name, info in self.cont.items():
            if query.lower() in name.lower() or query in info['ph_no']:
                res.append((name, info))
        return res

    def update_cont(self, name, ph_no, email, addr):
        if name in self.cont:
            self.cont[name] = {
                'ph_no': ph_no,
                'email': email,
                'addr': addr
            }
            print("Contact updated successfully.")
        else:
            print("Contact not found.")

    def del_cont(self, name):
        if name in self.cont:
            del self.cont[name]
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")

def main():
    contact_manager = ContMang()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            ph_no = input("Enter phone number: ")
            email = input("Enter email: ")
            addr = input("Enter address: ")
            contact_manager.add_cont(name, ph_no, email, addr)

        elif choice == '2':
            contact_manager.view_cont()

        elif choice == '3':
            query = input("Enter name or phone number to search: ")
            res = contact_manager.srch_cont(query)
            if res:
                print("Search results:")
                for name, info in res:
                    print(f"Name: {name}, Phone Number: {info['ph_no']}")
            else:
                print("No matching contacts found.")

        elif choice == '4':
            name = input("Enter the name of the contact to update: ")
            ph_no = input("Enter new phone number: ")
            email = input("Enter new email: ")
            addr = input("Enter new address: ")
            contact_manager.update_cont(name, ph_no, email, addr)

        elif choice == '5':
            name = input("Enter the name of the contact to delete: ")
            contact_manager.del_cont(name)

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
