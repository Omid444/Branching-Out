import json


USERS_FILE = "users.json"


def read_file():
    """Getting all users data at once"""
    with open(USERS_FILE, "r") as file:
        users = json.load(file)
        return users


def filter_users_by_name(name, users_file):
    """Filter users data base on name and print them"""
    filtered_users = [user for user in users_file if user["name"].lower() == name.lower()]
    if filtered_users:
        for user in filtered_users:
            print(user)
    else:
        print("***User not found in database***")


def filter_users_by_age(age, users_file):
    """Filter users data based on age and print them"""
    filtered_users = [user for user in users_file if user["age"] == age]

    if filtered_users:
        for user in filtered_users:
            print(user)
    else:
        print("***User not found in database***")


def filter_users_by_email(email, users_file):
    """Filter users data based on email address and print them"""
    filtered_users = [user for user in users_file if user["email"].lower() == email.lower()]

    if filtered_users:
        for user in filtered_users:
            print(user)
    else:
        print("***User not found in database***")


def main():
    users = read_file()  # loading all user data

    while True:
        filter_option = input("What would you like to filter by? ( name, age or email): ").strip().lower()

        if filter_option == "name":
            name_to_search = input("Enter a name to filter users:").strip()
            filter_users_by_name(name_to_search, users)

        elif filter_option == "age":
            try:
                age_to_search = int(input("Enter an age to filter users:").strip())
                filter_users_by_age(age_to_search, users)
            except ValueError:
                print("Please enter a valid number for age.")

        elif filter_option == "email":
            email_to_search = input("Enter a email to filter users:").strip()
            filter_users_by_email(email_to_search, users)

        else:
            print("***Filtering by that option is not yet supported***")


if __name__ == "__main__":
    main()