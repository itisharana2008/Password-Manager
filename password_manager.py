import json
import os
import hashlib
import base64

DATA_FILE = "data.json"


def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {"users": {}, "passwords": {}}


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def encode(text):
    """Simple reversible encoding for stored credentials."""
    return base64.b64encode(text.encode()).decode()


def decode(text):
    return base64.b64decode(text.encode()).decode()


def register(data):
    print("\n=== Register New User ===")
    username = input("Enter a username: ").strip()

    if username in data["users"]:
        print("❌ Username already exists.")
        return

    password = input("Create password: ").strip()
    data["users"][username] = hash_password(password)

    save_data(data)
    print("✅ Registration successful!")


def login(data):
    print("\n=== Login ===")
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    if username not in data["users"]:
        print("❌ No such user.")
        return None

    if data["users"][username] != hash_password(password):
        print("❌ Incorrect password.")
        return None

    print(f"🔓 Welcome, {username}!")
    return username


def add_password(username, data):
    print("\n=== Save a Credential ===")
    website = input("Website/Service: ")
    user = input("Login Email/Username: ")
    pwd = input("Password: ")

    data["passwords"].setdefault(username, [])
    data["passwords"][username].append({
        "website": website,
        "user": encode(user),
        "password": encode(pwd)
    })

    save_data(data)
    print("🔐 Credentials saved!")


def view_passwords(username, data):
    print("\n=== Your Saved Passwords ===")

    if username not in data["passwords"] or not data["passwords"][username]:
        print("📭 No saved passwords.")
        return

    for index, entry in enumerate(data["passwords"][username], start=1):
        print(f"\n{index}. {entry['website']}")
        print(f"   Username: {decode(entry['user'])}")
        print(f"   Password: {decode(entry['password'])}")


def main():
    data = load_data()

    while True:
        print("\n===== Password Manager =====")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose: ")

        if choice == "1":
            register(data)

        elif choice == "2":
            logged_user = login(data)
            if logged_user:
                while True:
                    print("\n--- Menu ---")
                    print("1. Add Credential")
                    print("2. View Credentials")
                    print("3. Logout")

                    user_choice = input("Choose: ")

                    if user_choice == "1":
                        add_password(logged_user, data)

                    elif user_choice == "2":
                        view_passwords(logged_user, data)

                    elif user_choice == "3":
                        print("🚪 Logged out.")
                        break

                    else:
                        print("❌ Invalid choice.")

        elif choice == "3":
            print("👋 Goodbye!")
            break

        else:
            print("❌ Invalid choice.")


if __name__ == "__main__":
    main()
