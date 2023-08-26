users = [{"user_name": "yy", "user_email": "yy", "user_password": "yy"}]

# users.append({"name": "hello", "email": "test@gmail.com"})

# for item in users:
#     print(item["name"])


class User:
    def __init__(self, user_name, user_email, user_password):
        self.user_name = user_name
        self.user_email = user_email
        self.user_password = user_password

    # printing password to verify if it is hashed or not
    def display_user_info(self):
        print(
            f"Username: {self.user_name}\n EmailId: {self.user_email}\n Password: {self.user_password}"
        )


# register user function which checks if the user is already present the users list, if not it appends the new user to the list
def register_user(user_name, user_email, user_password):
    for user in users:
        if user["user_email"] == user_email:
            print("Email already in use")
            return

    current_user = User(user_name, user_email, str(hash(user_password)))
    users.append(current_user)
    print("User registered successfully")
    return current_user


user_name = str(input("Enter your name: "))
user_email = str(input("Enter your email: "))
user_password = str(input("Enter your password: "))

new_user = register_user(user_name, user_email, user_password)

# if user was already present new_user will be empty
if new_user:
    new_user.display_user_info()