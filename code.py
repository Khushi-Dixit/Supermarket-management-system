#Supermarket Management System

class Supermarket:
    def __init__(self):
        self.inventory = {}  # Format: {product_name: [price, stock]}
        self.customers = {}  # Format: {customer_name: [purchased_items, total_spent]}

    # 1. Add product to inventory
    def add_product(self, product_name, price, stock):
        if product_name in self.inventory:
            self.inventory[product_name][1] += stock
        else:
            self.inventory[product_name] = [price, stock]
        print(f'{stock} units of {product_name} added at Rs {price} each.')

    # 2. Display inventory
    def display_inventory(self):
        print("\nInventory:")
        for product, details in self.inventory.items():
            price, stock = details
            print(f'{product}: Rs {price} | Stock: {stock}')
    
    # 3. Handle customer purchase
    def customer_purchase(self, customer_name):
        total_cost = 0
        purchased_items = []

        while True:
            product_name = input("Enter product name (or 'done' to finish): ").strip()
            if product_name.lower() == 'done':
                break
            if product_name not in self.inventory:
                print(f"{product_name} is not available in the inventory.")
                continue

            quantity = int(input(f"Enter quantity of {product_name}: "))
            if self.inventory[product_name][1] < quantity:
                print(f"Sorry, only {self.inventory[product_name][1]} units available.")
                continue

            price = self.inventory[product_name][0]
            cost = price * quantity
            total_cost += cost

            # Update inventory
            self.inventory[product_name][1] -= quantity

            # Add to customer purchases
            purchased_items.append((product_name, quantity))

        # Update customer record
        if customer_name in self.customers:
            self.customers[customer_name][0].extend(purchased_items)
            self.customers[customer_name][1] += total_cost
        else:
            self.customers[customer_name] = (purchased_items, total_cost)

        # Print bill
        self.print_bill(customer_name, purchased_items, total_cost)

    # 4. Print bill
    def print_bill(self, customer_name, purchased_items, total_cost):
        print(f"\nBill for {customer_name}:")
        for item, quantity in purchased_items:
            price = self.inventory[item][0]
            print(f'{item}: {quantity} x Rs {price} = Rs {price * quantity}')
        print(f'Total amount to pay: Rs {total_cost}')

    # 5. Display customer purchases
    def display_customer_purchases(self, customer_name):
        if customer_name not in self.customers:
            print(f'No record found for {customer_name}.')
            return
        print(f'\n{customer_name} Purchases:')
        for item, quantity in self.customers[customer_name][0]:
            print(f'{item}: {quantity}')
        print(f'Total spent: Rs {self.customers[customer_name][1]}')

    # 6. Generate daily report
    def generate_report(self):
        print("\nDaily Report:")
        for customer, details in self.customers.items():
            purchases, total_spent = details
            print(f'{customer}: Rs {total_spent} spent.')
        total_revenue = sum(details[1] for details in self.customers.values())
        print(f'Total revenue for the day: Rs {total_revenue}')


# Main program
def main():
    supermarket = Supermarket()

    # Input inventory details
    print("Enter products to add to the inventory:")
    while True:
        product_name = input("Enter product name (or 'done' to finish): ").strip()
        if product_name.lower() == 'done':
            break
        price = float(input(f"Enter price of {product_name}: "))
        stock = int(input(f"Enter stock of {product_name}: "))
        supermarket.add_product(product_name, price, stock)

    while True:
        print("\n1. Display Inventory")
        print("2. Customer Purchase")
        print("3. Display Customer Purchases")
        print("4. Generate Daily Report")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            supermarket.display_inventory()

        elif choice == '2':
            customer_name = input("Enter customer name: ")
            supermarket.customer_purchase(customer_name)

        elif choice == '3':
            customer_name = input("Enter customer name: ")
            supermarket.display_customer_purchases(customer_name)

        elif choice == '4':
            supermarket.generate_report()

        elif choice == '5':
            print("Exiting system...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
