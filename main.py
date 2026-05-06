import products
import store


# setup initial stock of inventory
product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250)
               ]
best_buy = store.Store(product_list)


def show_products():
    # show all products in the store
    all_products = best_buy.get_all_products()
    for i, product in enumerate(all_products, 1):
        print(f"{i}. ", end="")
        product.show()

def start():
    # main menu with options to list all products, show total amount in the store, make an order, or exit
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
                        quantity = int(input(f"Enter the quantity of {product.name}: "))
                        if quantity > product.get_quantity():
                            print(f"Insufficient quantity of {product.name}.")
                            continue
                        elif quantity <= 0:
                            print("Invalid quantity. Please enter a positive number.")
                            continue

                        shopping_list.append((product, quantity))
                    else:
                        print("Invalid product number. Please try again.")
                except ValueError:
                    print("Invalid input. Please enter a valid product number or 'q' to quit.")

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

start()
