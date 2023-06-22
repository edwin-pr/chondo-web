# Shopping cart program

# Create an empty dictionary to store items and their prices
shopping_cart = {}
print("Welcome to our shopping cart")
# Create a function to add items to the cart
def add_item(item, price):
    shopping_cart[item] = price
    print(f"{item} has been added to the cart.")

# Create a function to remove items from the cart
def remove_item(item):
    if item in shopping_cart:
        del shopping_cart[item]
        print(f"{item} has been removed from the cart.")
    else:
        print(f"{item} is not in the cart.")

# Create a function to calculate the total price
def calculate_total():
    total = sum(shopping_cart.values())
    print(f"Total price: ${total}")

# Main program loop
while True:
    print("--- Shopping Cart Menu ---")
    print("1. Add item")
    print("2. Remove item")
    print("3. Calculate total")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        item = input("Enter the item name: ")
        price = float(input("Enter the price: "))
        add_item(item, price)
    elif choice == "2":
        item = input("Enter the item name: ")
        remove_item(item)
    elif choice == "3":
        calculate_total()
    elif choice == "4":
        print("Thank you for using the shopping cart.")
        break
    else:
        print("Invalid choice. Please try again.")
