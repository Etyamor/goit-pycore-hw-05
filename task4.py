class MyException(Exception):
    pass


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except MyException as e:
            return f"CustomException occurred: {str(e)}"
    return inner


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, contacts):
    if len(args) < 2:
        raise MyException("Not enough arguments")
    name, phone = args
    if not phone.isdigit():
        raise MyException("Phone number should contain only digits")
    contacts[name] = phone
    return "Contact added"


@input_error
def change_contact(args, contacts):
    if len(args) < 2:
        raise MyException("Not enough arguments")
    name, phone = args
    if name not in contacts:
        raise MyException("Contact not found")
    if not phone.isdigit():
        raise MyException("Phone number should contain only digits")
    contacts[name] = phone
    return "Contact changed"


@input_error
def return_phone(args, contacts):
    if len(args) < 1:
        raise MyException("Not enough arguments")
    username = args[0]
    if username not in contacts:
        raise MyException("Contact not found")
    return contacts[username]


def return_all_contacts(contacts):
    max_key_length = max(len(str(key)) for key in contacts)
    for key, value in contacts.items():
        print(f"{str(key):<{max_key_length}} : {value}")

def main():
    contacts = {"Maksym": "0682082130"}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(return_phone(args, contacts))
        elif command == "all":
            return_all_contacts(contacts)
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
