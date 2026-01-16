from abc import ABC, abstractmethod

CURRENT_YEAR = 2025


class User(ABC):
    def __init__(self, name, account_year):
        self.name = name
        self.account_year = account_year

    def account_age(self):
        return CURRENT_YEAR - self.account_year

    @abstractmethod
    def get_role(self):
        pass


class Admin(User):
    def get_role(self):
        return "Admin"

    def __str__(self):
        return (
            f"Admin User: {self.name} | "
            f"Account Age: {self.account_age()} years"
        )


class Guest(User):
    def get_role(self):
        return "Guest"

    def __str__(self):
        return (
            f"Guest User: {self.name} | "
            f"Account Age: {self.account_age()} years"
        )
# Create objects
admin_user = Admin("Alice", 2019)
guest_user = Guest("Bob", 2023)
# Print role and account 
print(admin_user.get_role(), "-", admin_user.account_age(), "years")
print(guest_user.get_role(), "-", guest_user.account_age(), "years")

print(admin_user)
print(guest_user)
