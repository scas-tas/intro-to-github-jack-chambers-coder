
def add_item(inventory, name, quantity) -> None:
    if name in inventory:
        inventory[name] += quantity
    else:
        inventory[name] = quantity
    inv = inventory
def remove_item(inventory: dict, name: str, quantity: int) -> None:
    if name in inventory:
        inventory[name] = max(0, inventory[name] - quantity)
 
def get_stock_report(inventory: dict) -> str:
    for fruit in inventory:
        if inventory[fruit] > 0:
            print(f"{fruit}: {inventory[fruit]}")

inv = {}
add_item(inv, 'apples', 10)
add_item(inv, 'bananas', 5)
get_stock_report(inv)
add_item(inv, 'apples', 5)
remove_item(inv, 'bananas', 10)
get_stock_report(inv)
remove_item(inv, 'oranges', 3)
get_stock_report(inv)