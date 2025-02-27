class Subject:
    def __init__(self):
        self.observers = []

    def register(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)

    def unregister(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def notify_all(self):
        for observer in self.observers:
            observer.update(self)

# Concrete Subject (Product)
class Product(Subject):
    def __init__(self, product_name):
        super().__init__()
        self.name = product_name
        self.in_stock = False

    def set_availability(self, status):
        self.in_stock = status
        if self.in_stock:
            print(f"Product [{self.name}] is back in stock! Notifying customers...\n")
            self.notify_all()

# Observer Interface
class Observer:
    def update(self, product):
        pass

# Concrete Observer (Customer)
class Customer(Observer):
    def __init__(self, customer_name):
        self.name = customer_name

    def update(self, product):
        print(f"Notification sent to customer [{self.name}]: {product.name} is back in stock!")

# Driver code
if __name__ == "__main__":
    # Create product
    ps5 = Product("PlayStation 5")

    # Create customers
    customer1 = Customer("John")
    customer2 = Customer("Sneha")
    customer3 = Customer("Rahul")

    # Customers subscribing for notifications
    ps5.register(customer1)
    ps5.register(customer2)
    ps5.register(customer3)

    # Product becomes available
    ps5.set_availability(True)

    # Unregistering a customer (e.g. after notification or manually by customer)
    ps5.unregister(customer3)

    # Product availability again changed
    ps5.set_availability(False) # Out of stock again
    ps5.set_availability(True) # Back in stock again, notify remaining subscribers