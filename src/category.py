class Category:

    categories_count = 0
    products_count = 0

    def __init__(self, name: str, description: str, products: list) -> None:
        self.name = name
        self.description = description
        self.products = products
        Category.categories_count += 1
        Category.products_count += self.get_total_products_count()

    def get_total_products_count(self) -> int:
        total_count = 0
        for product in self.products:
            total_count += product.quantity
        return total_count
