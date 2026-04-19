#Q1

# class BankAccount():
#     def __init__(self, account_number, owner_name, balance):
#         self.accnum = account_number
#         self.name = owner_name
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount
#         print(f"{amount} deposited. New balance: {self.balance}")

#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Insufficient balance!")
#         else:
#             self.balance -= amount
#             print(f"{amount} withdrawn. New balance: {self.balance}")

#     def check_balance(self):
#         print(f"Current balance: {self.balance}")

#Q2.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__reviews = []   # encapsulated (private)

    # add a new review
    def add_review(self, review):
        self.__reviews.append(review)

    # count reviews
    def count_reviews(self):
        return len(self.__reviews)

    # display all reviews
    def display_reviews(self):
        if not self.__reviews:
            print("No reviews yet.")
        else:
            for i, review in enumerate(self.__reviews, 1):
                print(f"{i}. {review}")