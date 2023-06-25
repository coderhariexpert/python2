def display_menu():
    print("1. Append element")
    print("2. Extend list")
    print("3. Sort list")
    print("4. Sort list in reverse")
    print("5. Insert element")
    print("6. Count element")
    print("7. Get index")
    print("8. Pop element")
    print("9. Remove element")
    print("10. Reverse list")
    print("11. Exit")


def append_element(lst):
    element = input("Enter the element to append: ")
    lst.append(element)
    print("Element appended successfully!")


def extend_list(lst):
    elements = input("Enter the elements to extend the list (comma-separated): ")
    elements = [elem for elem in elements.split(",")]
    lst.extend(elements)
    print("List extended successfully!")


def sort_list(lst):
    lst.sort()
    print("List sorted successfully!")


def sort_list_reverse(lst):
    lst.sort(reverse=True)
    print("List sorted in reverse successfully!")


def insert_element(lst):
    index = int(input("Enter the index to insert the element: "))
    element = input("Enter the element to insert: ")
    lst.insert(index, element)
    print("Element inserted successfully!")


def count_element(lst):
    element = input("Enter the element to count: ")
    count = lst.count(element)
    print("Count:", count)


def get_index(lst):
    element = input("Enter the element to get the index: ")
    if element in lst:
        index = lst.index(element)
        print("Index:", index)
    else:
        print("Element not found in the list.")


def pop_element(lst):
    index = input("Enter the index to pop (leave empty for last element): ")
    if index == "":
        popped_element = lst.pop()
    else:
        popped_element = lst.pop(int(index))
    print("Popped element:", popped_element)


def remove_element(lst):
    element = input("Enter the element to remove: ")
    if element in lst:
        lst.remove(element)
        print("Element removed successfully!")
    else:
        print("Element not found in the list.")


def reverse_list(lst):
    lst.reverse()
    print("List reversed successfully!")


def get_user_list():
    elements = input("Enter the initial elements of the list (comma-separated): ")
    user_list = [elem.strip() for elem in elements.split(",")]
    return user_list


my_list = get_user_list()

while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        append_element(my_list)
    elif choice == "2":
        extend_list(my_list)
    elif choice == "3":
        sort_list(my_list)
    elif choice == "4":
        sort_list_reverse(my_list)
    elif choice == "5":
        insert_element(my_list)
    elif choice == "6":
        count_element(my_list)
    elif choice == "7":
        get_index(my_list)
    elif choice == "8":
        pop_element(my_list)
    elif choice == "9":
        remove_element(my_list)
    elif choice == "10":
        reverse_list(my_list)
    elif choice == "11":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")

    print("Updated List:", my_list)
    print()

