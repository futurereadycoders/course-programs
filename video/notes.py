print("Welcome to Notes!")
notes = {}
def main():
    while True:
        print("\n\nChoose an option: ")
        choice = input("Enter 1 to view all notes, 2 to add a note, 3 to delete a note, 4 to quit: \n")
        if choice == "1":
            display_notes()
        if choice == "2":
            add_note()
        if choice == "3":
            delete_note()
        if choice == "4":
            exit()
        else:
            print("Invalid choice. Please try again.")

def display_notes():
    if len(notes) == 0:
        print("No notes found.")
        main()
    print("Here are your notes:")
    for key in notes:
        print(f"{key}")
    choice = input("Enter the name of a note to view it, or type 'back' to go back.")
    if choice == "back":
        main()
    elif choice in notes:
        print(notes[choice])
        main()
    else:
        print("Note is not found.")
        display_notes()

def add_note():
    print("Enter the name of the note: ")
    name = input()
    print("Enter the contents of this new note: ")
    content = input()
    notes[name] = content
    print("Note added!")
    main()

def delete_note():
    print("Enter the name of the note to delete: ")
    name = input()
    if name in notes:
        del notes[name]
        print("Note deleted.")
    else:
        print("Note not found.")
    main()

main()

