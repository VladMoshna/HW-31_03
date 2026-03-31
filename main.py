import re

# zavd 1
def task1():
    with open("data.txt", "w") as f:
        for i in range(3):
            line = input(f"Enter line {i+1}: ")
            f.write(line + "\n")
    print("Saved to data.txt")


# zavd 2
def task2():
    words = {}

    try:
        with open("log.txt", "r") as f:
            text = f.read().lower()
            found_words = re.findall(r'\b\w+\b', text)

        for word in found_words:
            words[word] = words.get(word, 0) + 1

        top_10 = sorted(words.items(), key=lambda x: x[1], reverse=True)[:10]

        with open("word_stats.txt", "w") as f:
            for word, count in top_10:
                f.write(f"{word} - {count}\n")

        print("Saved to word_stats.txt")

    except FileNotFoundError:
        print("log.txt not found.")


# zavd 3
def add_order():
    number = input("Order number: ")
    product = input("Product name: ")
    qty = input("Quantity: ")
    price = input("Price: ")
    with open("orders.txt", "a") as f:
        f.write(f"{number},{product},{qty},{price}\n")


def view_orders():
    try:
        with open("orders.txt", "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("No orders found.")


def search_order():
    number = input("Enter order number: ")
    found = False
    with open("orders.txt", "r") as f:
        for line in f:
            if line.startswith(number + ","):
                print(line.strip())
                found = True
    if not found:
        print("Order not found.")


def update_order():
    number = input("Enter order number: ")
    lines = []
    updated = False

    with open("orders.txt", "r") as f:
        for line in f:
            if line.startswith(number + ","):
                parts = line.strip().split(",")
                qty = input("New quantity: ")
                price = input("New price: ")
                lines.append(f"{parts[0]},{parts[1]},{qty},{price}\n")
                updated = True
            else:
                lines.append(line)

    with open("orders.txt", "w") as f:
        f.writelines(lines)

    if updated:
        print("Order updated.")
    else:
        print("Order not found.")


def delete_order():
    number = input("Enter order number: ")
    lines = []
    deleted = False

    with open("orders.txt", "r") as f:
        for line in f:
            if not line.startswith(number + ","):
                lines.append(line)
            else:
                deleted = True

    with open("orders.txt", "w") as f:
        f.writelines(lines)

    if deleted:
        print("Order deleted.")
    else:
        print("Order not found.")


def task3():
    while True:
        print("\n--- Orders Menu ---")
        print("1. Add order")
        print("2. View orders")
        print("3. Search order")
        print("4. Update order")
        print("5. Delete order")
        print("6. Back to main menu")

        choice = input("Choose: ")

        if choice == "1":
            add_order()
        elif choice == "2":
            view_orders()
        elif choice == "3":
            search_order()
        elif choice == "4":
            update_order()
        elif choice == "5":
            delete_order()
        elif choice == "6":
            break
        else:
            print("Invalid choice.")


while True:
    print("\n=== MAIN MENU ===")
    print("1. Task 1 (data.txt)")
    print("2. Task 2 (word_stats.txt)")
    print("3. Task 3 (orders.txt)")
    print("4. Exit")

    choice = input("Choose task: ")

    if choice == "1":
        task1()
    elif choice == "2":
        task2()
    elif choice == "3":
        task3()
    elif choice == "4":
        break
    else:
        print("Invalid choice.")