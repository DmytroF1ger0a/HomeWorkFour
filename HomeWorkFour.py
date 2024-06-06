contacts = {}

def add_contact(name, phone):
    contacts[name] = phone
    return "Contact added."

def change_contact(name, new_phone):
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    return "Contact not found."

def show_phone(name):
    if name in contacts:
        return contacts[name]
    return "Contact not found."

def show_all():
    if not contacts:
        return "No contacts found."
    return '\n'.join(f"{name}: {phone}" for name, phone in contacts.items())

def parse_input(user_input):
    parts = user_input.strip().lower().split()
    command = parts[0]
    args = parts[1:]
    return command, args

def main():
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            if len(args) == 2:
                name, phone = args
                print(add_contact(name, phone))
            else:
                print("Invalid arguments. Use: add [name] [phone]")
        elif command == "change":
            if len(args) == 2:
                name, new_phone = args
                print(change_contact(name, new_phone))
            else:
                print("Invalid arguments. Use: change [name] [new phone]")
        elif command == "phone":
            if len(args) == 1:
                name = args[0]
                print(show_phone(name))
            else:
                print("Invalid arguments. Use: phone [name]")
        elif command == "all":
            print(show_all())
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
