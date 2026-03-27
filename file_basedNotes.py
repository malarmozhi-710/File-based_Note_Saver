def write_note():
    note = input("📝 Enter your note: ")
    
    with open("notes.txt", "a") as file:
        file.write(note + "\n")
    
    print("✅ Note saved successfully!")

def read_notes():
    try:
        with open("notes.txt", "r") as file:
            content = file.read()
            
            if content.strip() == "":
                print("📭 No notes found.")
            else:
                print("\n📒 Your Notes:\n")
                print(content)
    except FileNotFoundError:
        print("❌ No notes file found. Please add a note first.")

def main():
    while True:
        print("\n📌 Notes Saver Menu")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            write_note()
        elif choice == "2":
            read_notes()
        elif choice == "3":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Try again.")

# Run the program
main()