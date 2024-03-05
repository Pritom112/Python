import json

class PasswordManager:
    def __init__(self, data_file='passwords.json'):
        self.data_file = data_file
        self.passwords = self.load_passwords()

    def load_passwords(self):
        try:
            with open(self.data_file, 'r') as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            return {}

    def save_passwords(self):
        with open(self.data_file, 'w') as file:
            json.dump(self.passwords, file, indent=2)

    def add_password(self, service, username, password):
        if service not in self.passwords:
            self.passwords[service] = {'username': username, 'password': password}
            self.save_passwords()
            print(f"Password for {service} added successfully.")
        else:
            print(f"Password for {service} already exists. Consider updating it instead.")

    def get_password(self, service):
        if service in self.passwords:
            entry = self.passwords[service]
            print(f"Service: {service}\nUsername: {entry['username']}\nPassword: {entry['password']}")
        else:
            print(f"Password for {service} not found.")

    def delete_password(self, service):
        if service in self.passwords:
            del self.passwords[service]
            self.save_passwords()
            print(f"Password for {service} deleted successfully.")
        else:
            print(f"Password for {service} not found.")


password_manager = PasswordManager()

while True:
    print("\nPassword Manager Menu:")
    print("1. Add Password")
    print("2. Get Password")
    print("3. Delete Password")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        service = input("Enter the service: ")
        username = input("Enter the username: ")
        password = input("Enter the password: ")
        password_manager.add_password(service, username, password)

    elif choice == '2':
        service = input("Enter the service: ")
        password_manager.get_password(service)

    elif choice == '3':
        service = input("Enter the service: ")
        password_manager.delete_password(service)

    elif choice == '4':
        print("Exiting Password Manager.")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")