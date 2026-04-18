# Global variables as required by the task [cite: 237]
cart = {}
total_items = 0


def add_to_cart(item, quantity):
    """Adds an item to the cart or increments its quantity[cite: 230]."""
    global cart, total_items

    if quantity <= 0:
        print("Error: Quantity must be a positive number.")[cite: 238]
        return

    # If item exists, increment; otherwise, add it [cite: 230]
    if item in cart:
        cart[item] += quantity
    else:
        cart[item] = quantity

    total_items += quantity
    print(f"Added {quantity} {item}(s). Total items: {total_items}")


def remove_from_cart(item, quantity):
    """Reduces item quantity and handles edge cases[cite: 232]."""
    global cart, total_items

    # Handle missing items or excessive quantity [cite: 232, 238]
    if item not in cart:
        print(f"Error: {item} is not in your cart.")
    elif quantity > cart[item]:
        print(f"Error: Quantity exceeds stock. You only have {cart[item]} {item}(s).")
    elif quantity <= 0:
        print("Error: Please provide a positive quantity to remove.")
    else:
        cart[item] -= quantity
        total_items -= quantity

        # Clean up if quantity reaches zero
        if cart[item] == 0:
            del cart[item]

        print(f"Removed {quantity} {item}(s). Total items: {total_items}")


def check_item(item):
    """Returns the item’s quantity or 0 if missing[cite: 234]."""
    return cart.get(item, 0)


def display_cart():
    """Prints all items and total_items neatly[cite: 235]."""
    print("\n--- Current Shopping Cart ---")
    if not cart:
        print("The cart is currently empty.")
    else:
        for item, qty in cart.items():
            print(f"Item: {item} | Quantity: {qty}")
    print(f"Total items in cart: {total_items}")
    print("-----------------------------\n")


# Testing the implementation
if __name__ == "__main__":
    add_to_cart("Apples", 3)
    add_to_cart("Bananas", 5)
    display_cart()
    remove_from_cart("Apples", 2)
    print(f"Quantity of Bananas: {check_item('Bananas')}")
    display_cart()