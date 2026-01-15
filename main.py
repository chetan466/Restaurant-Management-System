
# Menu dictionary
menu = {
    "pizza": 40,
    "pasta": 50,
    "salad": 70,
    "coffee": 80
}

name = input("Enter your  Name :")
print(f"Welcome {name} to our restaurant! Here's the menu:")

for item, price in menu.items():
    print(f"{item.capitalize()}: Rs{price}")

order_total = 0
order_list = []  # To store ordered items

while True:
    item = input("Enter the name of the item you want to order: ").lower()

    if item in menu:
        order_total += menu[item]
        order_list.append(item)
        print(f"'{item}' added to your order.")
    else:
        print(" Sorry, we don't have that item.")

    another = input("Do you want to add another item? (Yes/No): ").lower()
    if another != "yes":
        break

# Show total
print("\nYour final order summary:")
for item in order_list:
    print(f"- {item.capitalize()} : Rs{menu[item]}")
print(f"Total Amount: Rs{order_total}")


# File I/O Part (Saving order)

with open("orders.txt", "a") as file:
    file.write(f"New Order by {name}:\n")
    if item in order_list: 
        file.write(f"- {item.capitalize()} : Rs{menu[item]}\n")
    file.write(f"Total Amount of {name} is : Rs{order_total}\n")
    file.write("--------------------------\n")

print("\n Your order has been saved successfully to 'orders.txt'.")



