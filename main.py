import products
import store


# setup initial stock of inventory
product_list = [
    products.Product("MacBook Air M2", price=1450, quantity=100),
    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    products.Product("Google Pixel 7", price=500, quantity=250)
]


def initialize_store():
    """
    Initializes the store with the predefined product list.

    :return: A Store object containing the initial products.
    """
    best_buy = store.Store(product_list)
    return best_buy


def show_products():
    """
    Displays all products in the store with their index numbers.
    """
    all_products = initialize_store().get_all_products()
    for i, product in enumerate(all_products, 1):
        print(f"{i}. ", end="")
        product.show()


def main():
    """
    Displays and manages the main menu for the store, allowing users to
    interact with available options such as listing products, checking
    total quantity, making orders, or exiting the application.

    The function provides a continuous menu loop until the user chooses
    to exit. It allows:
    1. Listing all available products in the store and displaying each
       product's details.
    2. Showing the total quantity of all available items in storage.
    3. Making an order by selecting products and specifying quantities.
    4. Exiting the application.

    The product list and other operations depend on the functionalities
    provided by the `best_buy` object and its methods.

    :raises Exception: If an error occurs during the ordering process,
                       such as attempting to make an order with
                       incorrect quantities.
    """
    best_buy = store.Store(product_list)

    while True:
        print("")
        print("  STORE MENU  ")
        print("---------------------------------")
        print("1. List all products in the store")
        print("2. Show total amount in the store")
        print("3. Make an order")
        print("4. Exit")

        choice = input("Please choose an option: ")

        if choice.strip() == "1":
            all_products = best_buy.get_all_products()
            for product in all_products:
                product.show()
            print("\n")
        elif choice.strip() == "2":
            print(best_buy.get_total_quantity())
            print("\n")
        elif choice.strip() == "3":
            all_products = best_buy.get_all_products()
            shopping_list = []
            show_products()

            while True:
                choice = input("Enter the product number (or 'q' to quit): ")
                if choice.strip() == "q":
                    break
                try:
                    product_index = int(choice) - 1
                    if 0 <= product_index < len(all_products):
                        product = all_products[product_index]
                        quantity = int(input(
                            f"Enter the quantity of {product.name}: "))
                        if quantity > product.get_quantity():
                            print(
                                f"Insufficient quantity of {product.name}.")
                            continue
                        elif quantity <= 0:
                            print(
                                "Invalid quantity. Please enter a positive number.")
                            continue
                        shopping_list.append((product, quantity))
                    else:
                        print("Invalid product number. Please try again.")
                except ValueError:
                    print(
                        "Invalid input. Please enter a valid product number "
                        "or 'q' to quit.")
            if shopping_list:
                try:
                    total_price = best_buy.make_order(shopping_list)
                    print(f"Total price: {total_price}")
                except Exception as e:
                    print(f"Order failed: {e}")
            print("\n")
        elif choice.strip() == "4":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
