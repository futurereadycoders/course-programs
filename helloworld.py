print("Welcome to the Notes app!")
print("Please choose an option:")
notes = {} # Creates an empty dictionary called `notes`
def main():
    while True:
        print("\n\nPlease choose an option:")
        choice = input("Enter 1 to view all notes, 2 to add a note, 3 to delete a note, 4 to quit: \n")
        if choice == "1":
            display_notes() # Runs the function display_notes() (not made yet)
        if choice == "2":
            add_note() # Runs the function add_note() (not made yet)
        if choice == "3":
            delete_note() # Runs the function delete_note() (not made yet)
        if choice == "4":
            break # Quits the while loop, and exits the program
        else:
            print("Invalid choice. Please try again.") # Re-prompts the user

def display_notes():
    if len(notes) == 0: # If there are no notes, it can't display notes
        print("No notes found.")
        main() # Sends user back to the main() function to choose valid option
    print("Here are all your notes:")
    noteid = 1
    for key in notes: # Iterates over the note dictionary
        print(f"{noteid}. {key}") # Prints off each note's title
    choice = input("Enter the name of a note to view it, or type 'back' to go back: ")
    if choice == "back":
        main() # Send user back
    elif choice in notes: # If the choice does exist:
        print(notes[choice]) # Print their note
        main() # Send user back
    else:
        print("Note not found.")
        display_notes() # Go back to the start of the function

def add_note():
    print("Please enter the name of the note: ")
    name = input() # Stores the name of the new note
    print("Please enter the contents of the note: ")
    content = input() # Stores the content of the new note
    notes[name] = content # Stores the content as the value of the name key
    print("Note added.")
    main() # Send user back to start

def delete_note():
    print("Please enter the name of the note to delete: ")
    name = input()
    if name in notes: # If the note exists:
        del notes[name] # Delete the note
        print("Note deleted.")
    else:
        print("Note not found.")
    main() # Go back to the start

main() # Run the main() function
