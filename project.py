
inventory = []
next_id_num = 101

def get_next_id():
    global next_id_num
    item_id = f"I{next_id_num}"
    next_id_num += 1
    return item_id

def validate_inputs(quantity, price):
    if not isinstance(quantity, int) or quantity < 0:
        print("Invalid quantity. Quantity must be a non-negative whole number. Item not added.")
        return False
    if price < 0:
        print("Invalid price. Price must be non-negative.")
        return False
    return True

def add_item(name, quantity, price):
    if not validate_inputs(quantity, price):
        return None
    
    item_id = get_next_id()
    new_item = {
        "id": item_id,
        "name": name,
        "quantity": quantity,
        "price": price
    }
    inventory.append(new_item)
    
    print(f"Item added. ID: {item_id} | {name} | Qty: {quantity} | Price: {price}")
    if quantity < 5:
        print(f"Low stock alert: {name} ({quantity})")
    return item_id

def view_inventory():
    if not inventory:
        print("Inventory is empty.")
        return
    print("-" * 50)
    print(f"{'ID':<6} | {'Name':<15} | {'Qty':<6} | {'Price':<8}")
    print("-" * 50)
    for item in inventory:
        print(f"{item['id']:<6} | {item['name']:<15} | {item['quantity']:<6} | {item['price']:<8}")
    print("-" * 50)

def update_item(item_id, quantity=None, price=None):
    for item in inventory:
        if item["id"] == item_id:
            if quantity is not None:
                if isinstance(quantity, int) and quantity >= 0:
                    item["quantity"] = quantity
                else:
                    print("Invalid quantity structure.")
                    return
            if price is not None:
                if price >= 0:
                    item["price"] = price
            print(f"Item {item_id} updated successfully.")
            return
    print(f"Item ID {item_id[1:] if item_id.startswith('I') else item_id} not found.")

def delete_item(item_id):
    global inventory
    initial_length = len(inventory)

    item_name = ""
    for item in inventory:
        if item["id"] == item_id:
            item_name = item["name"]
            break
            
    inventory = [item for item in inventory if item["id"] != item_id]
    
    if len(inventory) < initial_length:
        print(f"Item '{item_name}' deleted. Items left: {len(inventory)}")
    else:
        print(f"Item ID {item_id} not found.")

def show_total_stock_value():
    total_value = sum(item["quantity"] * item["price"] for item in inventory)
    breakdown = " | ".join([f"{item['name']}: {item['quantity'] * item['price']}" for item in inventory])
    print(f"(a) {breakdown}")
    print(f"Total stock value: {total_value}")

def show_low_stock_report():
    low_stock_items = [item for item in inventory if item["quantity"] < 5]
    if low_stock_items:
        items_str = " | ".join([f"{item['name']} | Qty: {item['quantity']}" for item in low_stock_items])
        print(f"(b) Low stock (below 5): {low_stock_items[0]['id']} | {items_str}")
    else:
        print("(b) No low stock items.")

print("--- Running Test Case 1 ---")
add_item("Pen", 50, 10)

print("\n--- Running Test Case 2 ---")
add_item("Eraser", 0, 5)
print("\n--- Running Test Case 3 ---")
add_item("Pencil", -5, 4)
update_item("I1999")
print("\n--- Running Test Case 4 ---")
inventory.clear()
next_id_num = 101
add_item("Pen", 50, 10)
add_item("Notebook", 3, 40)
print("\nExecuting Option 5 (Total stock value):")
show_total_stock_value()
print("\nExecuting Option 6 (Low stock report):")
show_low_stock_report()
print("\nExecuting Option 4 (Delete ID I101):")
delete_item("I101")
