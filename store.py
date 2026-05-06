from products import Product


class Store:
    def __init__(self, products):
        self.products = products


    def add_product(self, products):
        if not isinstance(products, Product):
            raise ValueError("Only Product instances can be added.")
        self.products.append(products)


    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)
        else:
            raise ValueError("Product not found in the store.")


    def get_total_quantity(self):
        total_quantity = 0
        for product in self.products:
            total_quantity += product.get_quantity()
        return total_quantity


    def get_all_products(self):
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)
        return active_products


    def order(self, shopping_list):
        total_price = 0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price
