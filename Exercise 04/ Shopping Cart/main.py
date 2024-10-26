class Product:
    def __init__(self, name, price, quantity):
        """Initialize a product with a name, price, and quantity."""
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        """Return string representation of the product."""
        return f"{self.name} - Price: ${self.price:.2f}, Quantity: {self.quantity}"


class ShoppingCart:
    def __init__(self):
        """Initialize an empty shopping cart."""
        self.cart = {}  # Dictionary to hold products in the cart

    def add_product(self, product):
        """Add a product to the cart. If it already exists, update the quantity."""
        if product.name in self.cart:
            self.cart[product.name]['quantity'] += product.quantity
        else:
            self.cart[product.name] = {'price': product.price, 'quantity': product.quantity}
        print(f"Added {product.quantity} of '{product.name}' to the cart.")

    def remove_product(self, product_name, quantity):
        """Remove a specified quantity of a product from the cart."""
        if product_name in self.cart:
            if quantity >= self.cart[product_name]['quantity']:
                del self.cart[product_name]  # Remove product if quantity is zero or less
                print(f"Removed '{product_name}' from the cart.")
            else:
                self.cart[product_name]['quantity'] -= quantity
                print(f"Removed {quantity} of '{product_name}' from the cart.")
        else:
            print(f"Product '{product_name}' not found in the cart.")

    def calculate_total(self):
        """Calculate and return the total price of the items in the cart."""
        total = sum(item['price'] * item['quantity'] for item in self.cart.values())
        return total

    def display_cart(self):
        """Display the contents of the shopping cart."""
        if not self.cart:
            print("The shopping cart is empty.")
            return

        print("\nShopping Cart Contents:")
        for product_name, details in self.cart.items():
            print(f"{product_name} - Price: ${details['price']:.2f}, Quantity: {details['quantity']}")
        print(f"Total Price: ${self.calculate_total():.2f}")


def main():
    """Main program loop for the shopping cart."""
    shopping_cart = ShoppingCart()

    while True:
        print("\n--- Shopping Cart ---")
        print("1. Add Product")
        print("2. Remove Product")
        print("3. Display Cart")
        print("4. Calculate Total Price")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter product name: ")
            price = float(input("Enter product price: $"))
            quantity = int(input("Enter product quantity: "))
            product = Product(name, price, quantity)
            shopping_cart.add_product(product)

        elif choice == '2':
            name = input("Enter product name to remove: ")
            quantity = int(input("Enter quantity to remove: "))
            shopping_cart.remove_product(name, quantity)

        elif choice == '3':
            shopping_cart.display_cart()

        elif choice == '4':
            total = shopping_cart.calculate_total()
            print(f"Total Price of items in the cart: ${total:.2f}")

        elif choice == '5':
            print("Exiting Shopping Cart. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
