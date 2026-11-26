


inventory = {}
def add_item(name, quantity):
    if name in inventory: 
        inventory[name] = inventory[name] + quantity
    else:
            inventory[name] = quantity

def remove_item(name):
    if name in inventory:
        del inventory[name]
    else:
        print("Item not found in inventory.")
def view_inventory():
    for name, quantity in inventory.items():
        print(name, ":", quantity)

while True:
    print("1) Add 2) Remove 3) View 4) Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        name = input("Enter item name: ")
        try:
            quantity = int(input("Enter quantity: "))
            add_item(name, quantity)
        except ValueError:
            print("Please enter a valid number for quantity.")
    elif choice == "2":
        name = input("Item name to remove: ")
        remove_item(name)
    elif choice == "3":
        view_inventory()
    elif choice == "4":
        break
    else:
        print("Invalid option. Choose 1-4.")
