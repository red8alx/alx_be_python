def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            item = input("Enter the item to be added into the shoping list: ")
            shopping_list.append(item)
            print(f"The Item \"{item}\" is added to Shoping List")
        elif choice == '2':
            # Prompt for and remove an item
            item = input("Enter the item to be removed from the shopping list: ")
            shopping_list.remove(item)
            print(f"The Item \"{item}\" is removed from the Shoping List")
            pass
        elif choice == '3':
            # Display the shopping list
            print(f"The  items in the Shopping List are: {shopping_list}")
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()