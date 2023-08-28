# LOAD products list from products.txt
import os
import json
import time
import csv




# Load product list fron product.txt
#current_dir_product_list = os.path.dirname(os.path.abspath(__file__))
#product_list_path = os.path.join(current_dir_product_list, 'notes', 'products.txt')


with open("./notes/products.csv", 'r') as file:
    product_list = list(csv.DictReader(file))

# LOAD couriers list from couriers.txt
#current_dir = os.path.dirname(os.path.abspath(__file__))
#courier_list_path = os.path.join(current_dir, 'notes', 'couriers.txt')

#with open(courier_list_path, 'r') as file:
#    courier_list = file.readlines()
with open("./notes/couriers.csv", 'r') as file:
    courier_list = list(csv.DictReader(file))

# LOAD order list from Orders_list.csv
#with open("./notes/Orders_list.json", "r") as file:
#    order_list = json.load(file)
with open("./notes/Orders_list.csv", 'r') as file:
    order_list = list(csv.DictReader(file))


## Create function of all pages
# Main menu function
def print_menu():
    clear_terminal()
    print("""
    - - - - - - - - - -
    Welcome to CAFE SHOP
    - - - - - - - - - -
    Main Menu Options:
    
    0. Exit
    1. Product Menu
    2. Courier Menu
    3. Orders Menu
    """)
## Saving product list when exiting
def save_products_list():
    fieldnames = ['Product ID', 'Product name', 'Price']
    with open("./notes/products.csv", 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(product_list)

## Saving couriers list when exiting
def save_couriers_list():
    fieldnames = ['Courier ID', 'Courier name', 'Phone number']
    with open("./notes/couriers.csv", 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(courier_list)

## Saving Order list json when exiting
#def save_order_list():
#    data = {"Order" : Orders}
#    with open("./notes/Orders_list.json", "w") as file:
#        json.dump(data, file, indent=5)

## Saving Order list csv when exiting
def save_order_list():
    fieldnames = ['Customer name', 'Customer address', 'Customer phone', 'Courier', 'Status', 'Items']
    with open("./notes/Orders_list.csv", "w", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for order in order_list:
            writer.writerow({
                'Customer name': order['Customer name'],
                'Customer address': order['Customer address'],
                'Customer phone': order['Customer phone'],
                'Courier': order['Courier'],
                'Status': order['Status'],
                'Items': ', '.join(order['Items'])
            })

# Function to clear the terminal
def clear_terminal():
    time.sleep(0.5)
    os.system('cls' if os.name == 'nt' else 'clear')
 
# Product menu function
def print_product_menu():
    clear_terminal()
    print("""
    - - - - - - - - - -
         PRODUCT MENU
    - - - - - - - - - -
    """)
    print("Product Menu Options:")
    print("0. Return to Main Menu")
    print("1. Print Products")
    print("2. Create New Product")
    print("3. Update Existing Product")
    print("4. Delete Product")

# Functions of Product menu subfolders
def print_products():
    clear_terminal()
    if not product_list:
        print("No products available.")
        return
    else:
        clear_terminal()
        print("Products: ")
        print("0. Return to Product Menu")
        for i, product in enumerate(product_list, start=1):
            print(f"{i}. {product}")

        while True:
            try:
                index = int(input("To return to the previous menu, press - 0): ")) - 1
                clear_terminal()
                if index == -1:
                    return int(index)
                elif index < 0 or index >= len(product_list):
                    print("Invalid index.")

            except ValueError:
                print("This is input invalid, please select a valid number")

# Create product function
unic_product_number = 0

def create_product():
    global unic_product_number
    clear_terminal()
    new_product_name = input("Enter product name: ")
    new_product_price = float(input("Enter product price: "))
    new_product_price_with_pound = '£' + str(new_product_price)
    unic_product_number += 1
    new_product = {
        'Product ID': unic_product_number,
        'Product name': new_product_name,
        'Price': str(new_product_price_with_pound)
    }
    product_list.append(new_product)
    print("Product created.")

# Create product update function
def update_product():
    clear_terminal()
    if not product_list:
        print("No products available.")
        return
    else:
        clear_terminal()
        print("Select a product to update:")
        print("0. Return to Product List")
        for i, product in enumerate(product_list, start=1):
            print(f"{i}. {product}")
        
        while True:
            try:      
                index = int(input("Enter the number of the product: ")) - 1
                clear_terminal()
                if index == -1:
                    return int(index)
                elif index < 0 or index >= len(product_list):
                    print("Invalid index.")
                else:
                    index == 0 or index <= len(product_list)
                    print("1. Edit Name")
                    print("2. Edit Price")
                    
                    while True:
                        try:
                            edit_input = int(input("Please enter your choice: ")) - 1
                            clear_terminal()
                            if edit_input == 0:
                                new_name_product = str(input("Enter the new product name: "))
                                old_name_product = product_list[index]['Product name']
                                print(f'Are you sure update {old_name_product} to {new_name_product}')
                                print("1. Yes")
                                print("2. No")

                                while True:
                                    try:
                                        confirm_index = int(input("Please enter your choice: ")) - 1
                                        clear_terminal()
                                        if confirm_index == 0:                               
                                            product_list[index]['Product name'] = new_name_product
                                            print("Product name updated.")
                                            return
                                        elif confirm_index == 1:
                                            print("Update canceled")
                                            return
                                        else:
                                            print("Invalid choice try again")
                                    except ValueError:
                                        print("This is input invalid, please select a valid number")
                            elif edit_input == 1:
                                new_price_product = float(input("Enter the new price: "))
                                new_price_product_with_pound = '£' + str(new_price_product)
                                print(f'Are you sure update {product_list[index]["Price"]} to {new_price_product_with_pound} ?')
                                print("1. Yes")
                                print("2. No")

                                while True:
                                    try:
                                        confirm_index_price = int(input("Please enter your choice: ")) - 1
                                        clear_terminal()
                                        if confirm_index_price == 0:
                                            product_list[index]["Price"] = new_price_product_with_pound
                                            print("Product price updated.")
                                            return
                                        elif confirm_index_price == 1:
                                            print("Update canceled")
                                            return
                                        else:
                                            print("Invalid choice try again")
                                    except ValueError:
                                        print("This is input invalid, please select a valid number")
                        except ValueError:
                            print("This is input invalid, please select a valid number")
            except ValueError:
                print("This is input invalid, please select a valid number")


# Create product delete function
def delete_product():
    clear_terminal()
    if not product_list:
        print("No products available.")
        return
    else:
        clear_terminal()
        print("Products: ")
        print("0. Return to Product List")
        for i, product in enumerate(product_list, start=1):
            print(f"{i}. {product}")
        
        while True:
            try:
                index = int(input("Enter the number of the product: ")) - 1
                clear_terminal()
                if index == -1:
                    return int(index)
                elif index < 0 or index >= len(product_list):
                    print("Invalid index.")
                else:
                    delete_name_product = product_list[index]['Product name']
                    print(f'Are you sure delete {delete_name_product}')
                    print("1. Yes")
                    print("2. No")
                    while True:
                        try:
                            confirm_index = int(input("Please enter your choice: ")) - 1
                            clear_terminal()
                            if confirm_index == 0:
                                print(f'Product "{product_list[index]}" deleted successfuly')
                                del product_list[index]
                                print("Product deleted correctly")
                                return
                            elif confirm_index == 1:
                                print("Removing canceled")
                                return
                            else:
                                print("Invalid choice try again")
                        except ValueError:    
                            print("This is input invalid, please select a valid number")
            except ValueError:
                print("This is input invalid, please select a valid number")

## Couriers section
# Create couriers menu function
def print_courier_menu():
    clear_terminal()
    print("""
    - - - - - - - - - -
         COURIER MENU
    - - - - - - - - - -
    0. Return to Main menu
    1. Courier list
    2. Create new courier
    3. Update existing courier
    4. Delete courier
    """)
# Create couriers list function
def print_courier():
    clear_terminal()
    if not courier_list:
        print("No couriers available.")
        return
    else:
        clear_terminal()
        print("Couriers: ")
        print("0. Return to Product Menu")
        for i, courier in enumerate(courier_list, start=1):
            print(f'{i}: {courier}')

        while True:
            try:
                index = int(input("Enter courier number: ")) - 1
                clear_terminal()
                if index == -1:
                    return int(index)
                elif index < 0 or index >= len(courier_list):
                    print("Invalid index.")
                else:
                    index == 0 or index <= len(courier_list)
                    print("This function does not working yet, please wait litle bit more...")

            except ValueError:
                print("This is input invalid, please select a valid number")

# Create function to create a new courier
unic_courier_number = 0
def Print_create_new_courier():
    global unic_courier_number
    clear_terminal()
    new_courier_name = str(input("Enter new courier name: "))
    new_courier_phone = int(input("Enter phone number: "))
    unic_courier_number += 1
    new_courier = {
        'Courier ID': unic_courier_number,
        'Courier name': new_courier_name,
        'Phone number': str(new_courier_phone)
    }
    courier_list.append(new_courier)
    print("New courier added successfully.")

# Create update existing courier function
def print_update_existing_courier():
    clear_terminal()
    if not courier_list:
        print("No couriers available.")
        return
    else:
        clear_terminal()
        print("Select a courier to update:")
        print("0. Return to Courier menu")
        for i, courier in enumerate(courier_list, start=1):
            print(f'{i}: {courier}')
        
        while True:
            try:
                index = int(input("Select a courier to update: ")) - 1
                clear_terminal()
                if index == -1:
                    return int(index)
                elif index < 0 or index >= len(courier_list):
                    print("Invalid index.")
                else:
                    index == 0 or index <= len(courier_list)
                    print("1. Edit name")
                    print("2. Edit phone number")

                    while True:
                        try:
                            edit_input_courier = int(input("Please enter your choice: ")) - 1
                            clear_terminal()
                            if edit_input_courier == 0:
                                update_courier_name = str(input("Enter the new courier name: "))
                                old_name_courier = courier_list[index]['Courier name']
                                clear_terminal()
                                print(f'Are you sure update {old_name_courier} to {update_courier_name}')
                                print("1. Yes")
                                print("2. No")

                                while True:
                                    try:
                                        confirm_index = int(input("Please enter your choice: ")) - 1
                                        clear_terminal()
                                        if confirm_index == 0:
                                            courier_list[index]['Courier name'] = update_courier_name
                                            print("Name updated correctly")
                                            return
                                        elif confirm_index == 1:
                                            print("Update canceled")
                                            return
                                        else:
                                            print("Invalid choice try again")
                                    except ValueError:
                                        print("This is input invalid, please select a valid number")
                            elif edit_input_courier == 1:
                                new_phone_number = int(input("Enter new phone number: "))  
                                old_phone_courier = courier_list[index]['Phone number']  
                                clear_terminal()
                                print(f'Are you sure update {old_phone_courier} to {new_phone_number} ?')
                                print("1. Yes")
                                print("2. No")

                                while True:
                                    try:
                                        confirm_index_phone = int(input("Please enter your choice: ")) - 1
                                        clear_terminal()
                                        if confirm_index_phone == 0:
                                            courier_list[index]['Phone number'] = new_phone_number
                                            print("Courier number updated.")
                                            return
                                        elif confirm_index_phone == 1:
                                            print("Update canceled")
                                            return
                                        else:
                                            print("Invalid choice try again")
                                    except ValueError:
                                        print("This is input invalid, please select a valid number")
                        except ValueError:
                            print("This is input invalid, please select a valid number")
            except ValueError:
                print("This is input invalid, please select a valid number")

# Create delete courier function
def print_delete_courier():
    clear_terminal()
    if not courier_list:
        print("No couriers available.")
        return
    else:
        clear_terminal()
        print("Couriers: ")
        print("0. Return to Courier List")
        for i, courier in enumerate(courier_list, start=1):
            print(f'{i}: {courier}')

        while True:
            try:
                index = int(input("Select a courier to delete: ")) - 1
                clear_terminal()
                if index == -1:
                    return int(index)
                elif index < 0 or index >= len(courier_list):
                    print("Invalid index.")
                else:
                    index == 0 or index <= len(courier_list)
                    old_name_courier = courier_list[index]['Courier name']
                    clear_terminal()
                    print(f'Are you sure delete {old_name_courier} ?')
                    print("1. Yes")
                    print("2. No")

                    while True:
                        try:
                            confirm_index = int(input("Please enter your choice: ")) - 1
                            clear_terminal()
                            if confirm_index == 0:
                                #delete_courier = courier_list.pop(index)
                                #with open(courier_list_path, 'w') as file:
                                #    file.writelines(courier_list)
                                del courier_list[index]
                                print("Courier deleted correctly")
                                return
                            elif confirm_index == 1:
                                print("Removing canceled")
                                return
                            else:
                                print("Invalid choice try again")
                        except ValueError:
                            print("This is input invalid, please select a valid number")
            except ValueError:
                print("This is input invalid, please select a valid number")


## Order menu function
# Create empty Order list

# Create orders menu function
def print_orders_menu ():
    clear_terminal()
    print("""
    - - - - - - - - - -
         ORDER MENU
    - - - - - - - - - -
    0. Return to Main Menu
    1. View orders
    2. Create order
    3. Update existing order status
    4. Update existing order
    5. Delete order
    """)

# Create orders list function
def print_order_directory():
    clear_terminal()
    if not order_list:
        print("No orders available.")
        return
    else:
        clear_terminal()
        print("0. Return to Order Menu")
        print("Orders: ")
        print("___________")
        #for i, order in enumerate(order_list, start=1):
        #    print(f'{i}. Order')
        #    print("")
        #    print(f'Name: {order["customer_name"]}')
        #    print(f'Address: {order["customer_address"]}')
        #    print(f'Phone: {order["customer_phone"]}')
        #    print(f'Status: {order["status"]}')
        #    print(f'Courier ID: {order["courier"]}')
        #    print(f'Items: {order["items"]}')
        #    print("___________")
        for i, product in enumerate(order_list, start=1):
            print(f"{i}. {product}")
        while True:
            try:
                index = int(input("Enter order number(For this moment working just number 0): ")) - 1
                clear_terminal()
                if index == -1:
                    return int(index)
                elif index < 0 or index >= len(order_list):
                    print("Invalid index.")
                else:
                    index == 0 or index <= len(order_list)
                    print("This function does not working yet, please wait litle bit more...")  
            except ValueError:
                print("This is input invalid, please select a valid number")
# Create customer details function
def print_create_order():
    clear_terminal()
    input_customer_name = str(input("Enter your name: "))
    input_customer_address = str(input("Enter your address: "))
    input_customer_phone_number = int(input("Enter your phone number: "))

    # Print list of couriers
    clear_terminal()
    if not courier_list:
        print("No couriers available.")
        return
    else:
        clear_terminal()
        print("0. Return to COURIER LIST")
        print("Couriers: ")
        for i, courier in enumerate(courier_list, start=1):
            print(f'{i}: {courier}')

        while True:
            try:
                courier_index = int(input("Please select courier for your order: ")) - 1
                if courier_index == -1:
                    return int(courier_index)
                elif courier_index < 0 or courier_index >= len(courier_list):
                    print("Invalid index.")

                else:
                    if not product_list:
                        print("No products available.")
                        return
                    else:
                        clear_terminal()
                        print("Products: ")
                        print("0. Return to Product Menu")
                        for i, product in enumerate(product_list, start=1):
                            print(f"{i}. {product}")
                        
                        selected_product_indices = []
                        while True:
                            try:
                                product_index = int(input("Select a product number to add to your order: ")) - 1
                                clear_terminal()
                                if product_index == -1:
                                    return int(product_index)
                                elif product_index < 0 or product_index >= len(product_list):
                                    print("Invalid index.")
                                else:
                                    clear_terminal()
                                    selected_product_indices.append(product_index)
                                    print("""
                                    Order created successfully
                                    -------------------------
                                    Would like to add more products?
                                    1. Yes
                                    2. No
                                    """)
                                    choice = int(input("Enter your choice: "))
                                    if choice == 2:
                                        order = {
                                            'Customer name': input_customer_name,
                                            'Customer address': input_customer_address,
                                            'Customer phone': input_customer_phone_number,
                                            'Status': 'Preparing',
                                            'Courier': courier_list[courier_index]['Courier ID'],
                                            'Items': [product_list[i]['Product ID'] for i in selected_product_indices]
                                        }
                                    
                                        order_list.append(order)
                                        print("Order created successfuly")
                                        return
                                    elif choice != 1:
                                        print("Invalid choice. Returning to product menu.")
                                        return
                                    else:
                                        clear_terminal()
                                        print("Products: ")
                                        print("0. Return to Product Menu")
                                        for i, product in enumerate(product_list, start=1):
                                            print(f"{i}. {product}")
                            except ValueError:
                                print("This is input invalid, please select a valid number")

            except ValueError:
                print("This is input invalid, please select a valid number")

# Create update status function
def print_update_status():
    clear_terminal()
    if not order_list:
        print("No orders available")
        return
    else:
        clear_terminal()
        print("0. Return to previous menu")
        print("Select order to update")
        print("___________")
        for i, order in enumerate(order_list, start=1):
            print(f'{i}. {order}')
        while True:
            try:
                index = int(input("Pleas enter your choice: ")) - 1
                clear_terminal()
                if index == -1:
                    return int(index)
                elif index < 0 or index >= len(order_list):
                    print("Invalid choice")
                else:
                    clear_terminal()
                    print("""
                    0. Return Previous menu
                    _______________
                    Orders status:
                    1. Preparing
                    2. On delivery
                    3. Delivered
                    """)

                    while True:
                        try:
                            status_index = int(input("Pleas enter your new status of order: ")) - 1
                            clear_terminal()
                            if status_index == -1:
                                return int(index)
                            elif status_index == 1:
                                order_list[index]['Status'] = 'On Delivery'
                                print("Order status updated successfuly")
                                return
                            elif status_index == 2:
                                order_list[index]['Status'] = 'Delivered'
                                print("Order status updated successfuly")
                                return
                            elif status_index == 0:
                                order_list[index]['Status'] = 'Preparing'
                                print("Order status updated successfuly")
                                return
                            else:
                                print("Invalid choice")
                        except ValueError:
                            print("This is input invalid, please select a valid number")
            except ValueError:
                print("This is input invalid, please select a valid number")

# Create update function
def print_update_existing_order():
    clear_terminal()
    if not order_list:
        print("No orders available")
        return
    else:
        clear_terminal()
        print("0. Return to previous menu")
        print("Orders: ")
        print("___________")

        for i, order in enumerate(order_list, start=1):
            print(f'{i}. {order}')
        
        while True:
            try:
                index1 = int(input("Pleas enter your choice: ")) - 1
                clear_terminal()
                if index1 == -1:
                    return int(index1)
                elif index1 < 0 or index1 >= len(order_list):
                    print("Invalid choice")
                else:
                    clear_terminal()
                    print("""
                    0. Return to previous menu
                    __________________________
                    What do you want to update:
                    1. Name
                    2. Address
                    3. Phone number
                    4. Courier
                    """)
                    while True:
                        try:
                            index_updated = int(input("Pleas enter your choice: ")) - 1
                            clear_terminal()
                            if index_updated == -1:
                                return int(index1)
                            elif index_updated == 0:
                                new_name = str(input("Enter the new name: "))
                                order_list[index1]['Customer name'] = new_name
                                print("Order name updated successfuly")
                                return
                            elif index_updated == 1:
                                new_address = str(input("Enter the new address: "))
                                order_list[index1]['Customer address'] = new_address
                                print("Order address updated successfuly")
                                return
                            elif index_updated == 2:
                                new_phone = str(input("Enter the new phone number: "))
                                order_list[index1]['Customer phone'] = new_phone
                                print("Order phone updated successfuly")
                                return
                            elif index_updated == 3:
                                if not courier_list:
                                    print("No couriers available")
                                    return
                                else:
                                    clear_terminal()
                                    print("Couriers: ")
                                    print("0. Return to Product Menu")
                                    for i, courier in enumerate(courier_list, start=1):
                                        print(f'{i}: {courier}')

                                    while True:
                                        try:
                                            new_courier = int(input("Enter the new courier: ")) - 1
                                            clear_terminal()
                                            if new_courier == -1:
                                                return
                                            elif new_courier == 0 or new_courier <= len(courier_list):
                                                order_list[index1]['Courier'] = courier_list[new_courier]['Courier ID']
                                                print("Order courier name updated successfuly")
                                                return
                                            else:
                                                print("Invalid index")
                                        except ValueError:
                                            print("This is input invalid, please select a valid number")
                            else:
                                print("Invalid choice")
                        except ValueError:
                            print("This is input invalid, please select a valid number")
            except ValueError:
                print("This is input invalid, please select a valid number")

# Create delete order function
def print_delete_order():
    if not order_list:
        print("No orders available")
        return
    else:
        clear_terminal()
        print("0. Return to previous menu")
        print("Select order to delete")
        print("Orders:")
        for i, order in enumerate(order_list, start=1):
            print(f'{i}. {order}')
        
        while True:
            try:
                index = int(input("Select a order to delete: ")) - 1
                clear_terminal()
                if index == -1:
                    return int(index)
                elif index < 0 or index >= len(order_list):
                    print("Invalid choice")
                    return
                else:
                    index == 0 or index <= len(courier_list)
                    clear_terminal()
                    print(f'Are you sure delete order?')
                    print("1. Yes")
                    print("2. No")

                    while True:
                        confirm_index_order = int(input("Please enter your choice: ")) - 1
                        clear_terminal()
                        if confirm_index_order == 0:      
                            del order_list[index]
                            print("Order deleted.")
                            return
                        elif confirm_index_order == 1:
                            print("Removing canceled")
                            return
                        else:
                            print("Invalid choice try again")
            except ValueError:
                print("This is input invalid, please select a valid number")

# Main loop
while True:
    print_menu()
    user_input = input("Enter your choice: ")

    if user_input == "0":
        print("Saving products list....")
        save_products_list()
        print("Saving couriers list....")
        save_couriers_list()
        print("Saving order list....")
        save_order_list()
        print("Exiting the app.....")
        break
    elif user_input == "1":
        while True:
            print_product_menu()
            user_input_1 = input("Enter your choice: ")

            if user_input_1 == "0":
                break
            elif user_input_1 == "1":
                print_products()
            elif user_input_1 == "2":
                create_product()
            elif user_input_1 == "3":
                update_product()
            elif user_input_1 == "4":
                delete_product()
            else:
                print("Invalid choice. Please try again.")
    elif user_input == "2":
        while True:
            print_courier_menu()
            user_input_3 = input("Enter your choice: ")

            if user_input_3 == "0":
                break
            elif user_input_3 == "1":
                print_courier()
            elif user_input_3 == "2":
                Print_create_new_courier()
            elif user_input_3 == "3":
                print_update_existing_courier()
            elif user_input_3 == "4":
                print_delete_courier()
            else:
                print("Invalid choice. Please try again.")
    elif user_input == "3":
        while True:
            print_orders_menu()
            user_input_2 = input("Enter your choice: ")

            if user_input_2 == "0":
                break
            elif user_input_2 == "1":
                print_order_directory()
            elif user_input_2 == "2":
                print_create_order()
            elif user_input_2 == "3":
                print_update_status()
            elif user_input_2 == "4":
                print_update_existing_order()
            elif user_input_2 == "5":
                print_delete_order()
            else:
                print("Invalid choice. Please try again.")

    else:
        print("Invalid choice. Please try again.")