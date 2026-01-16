from abc import ABC, abstractmethod

class User(ABC):
    
    def __init__(self,name,joining_year):
     self.name = name
     self.joining_year = joining_year
     
    def years_on_plateform(self):
         current_year = 2024
         return current_year - self.joining_year
     
    @abstractmethod
    def role(self):
        pass

    def display_info(self):
        print(
            f'Name: {self.name}, Role: {self.role()}, Years on Platform: {self.years_on_plateform()}'
        )


class Customer(User):
     def role(self):
        return "Customer"
    
class Vendor(User):
     def role(self):
        return "Vendor"


# Example usage
customer = Customer("Alice", 2020)
vendor = Vendor("Bob", 2018)

customer.display_info()
vendor.display_info()
