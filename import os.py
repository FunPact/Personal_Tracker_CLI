import os

def load_data(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.read().strip().split('\n')
    data = []
    for line in lines:
        parts = line.split('|')
        if len(parts) == 2:
            data.append({'id': parts[0], 'text': parts[1]})
    return data

def save_data(filename, data):
    with open(filename, 'w', encoding='utf-8') as f:
        for item in data:
            f.write(f"{item['id']}|{item['text']}\n")

def print_menu():
    print("\nPersonal Tracker CLI")
    print("1. List items")
    print("2. Add an item")
    print("3. Update an item")
    print("4. Exit")

def list_items(data):
    if not data:
        print("No items found.")
        return
    print("Your items:")
    for item in data:
        print(f"{item['id']}: {item['text']}")

def add_item(data):
    text = input("Enter new item text: ").strip()
    if not text:
        print("Item text cannot be empty.")
        return
    new_id = str(max([int(item['id']) for item in data], default=0) + 1)
    data.append({'id': new_id, 'text': text})
    print(f"Added item with id {new_id}.")

def update_item(data):
    if not data:
        print("No items to update.")
        return
    id_to_update = input("Enter id of item to update: ").strip()
    matched = [item for item in data if item['id'] == id_to_update]
    if not matched:
        print(f"No item with id {id_to_update} found.")
        return
    new_text = input("Enter new text for the item: ").strip()
    if not new_text:
        print("New text cannot be empty.")
        return
    matched[0]['text'] = new_text
    print(f"Item {id_to_update} updated.")

def main():
    filename = 'personal_tracker.txt'
    data = load_data(filename)
    while True:
        print_menu()
        choice = input("Choose an option: ").strip()
        if choice == '1':
            list_items(data)
        elif choice == '2':
            add_item(data)
            save_data(filename, data)
        elif choice == '3':
            update_item(data)
            save_data(filename, data)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == '__main__':
    main()
