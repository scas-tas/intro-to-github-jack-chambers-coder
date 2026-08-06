
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
    report = ""
    for fruit in sorted(inventory):
        if inventory[fruit] > 0:
            report += (f"{fruit}: {inventory[fruit]}\n")
    return report.strip()
def mainline():
    inv = {}
    add_item(inv, 'apples', 10)
    add_item(inv, 'bananas', 5)
    print(get_stock_report(inv))
    add_item(inv, 'apples', 5)
    remove_item(inv, 'bananas', 10)
    print(get_stock_report(inv))
    remove_item(inv, 'oranges', 3)
    print(get_stock_report(inv)
    )
mainline()