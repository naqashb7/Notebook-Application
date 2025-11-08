import os


# Initation of the class "Notebook"
#The __init__ function is used here in the first method of the class

class Notebook:
    def __init__(self):
        self.notes = []


#Method to create a new note. This includes a note ID, note title and content. All fields are stored in a dictionary called notes.
#The storage is useful for later access for viewing, editing or deleting notes.
#In this method a dictionary is used to hold the information

    def create_note(self):
        note_id = input("Associate an ID to this note. Make sure you only use one Word and one number. Make sure it is unique: ")
        title = input("Give a Title to your note. This can be anything: ")
        content = input("Enter your note content: ")
        self.notes.append({"ID":note_id, "Title":title,"Content":content})
        print("Congratulations, your note has been created.")


#Method to view a note. First it must be determined if ANY notes exist. Once this is established then the appropriate note can be selected to view.



    def view_note(self):
        if not self.notes:
            print ("No Notes exist. Please create a note to continue")
        else:
            print("Current Available notes: ")
            for note in self.notes():
                print(f"ID: {note["ID"]}, Title: {note['Title']}")



#Method to edit existing notes. First the note must be selected from the ID and then the title and the content can be edited.


    def edit_note(self):
        note_id = input("Enter the ID of the note you want to edit: ")
        for note  in self.notes: 
            if note ['ID'] == note.id:
                new_title = input(f"Enter the new title for note id - {note_id}: ")
                new_content = input(f"ENter the new content for the note id - {note_id}: ")
                note['Title'] = new_title
                note['Content'] = new_content
                print (f"NOTICE: Note {note_id} has been edited. Please make sure edits are approved.")
                return
        print (f"No note with the following ID exists: {note_id}")


#Method to delete notes. First the note to be deleted has to be selected and then the deletion is confirmed.


    def delete_note(self):
        note_id = input("Enter the ID of the note you would like to delete: ")
        for note in self.notes:
            if note['ID'] == note_id:
                confirmation = input(f"Are you sure you would like to delete{note_id} ? (Y or N)")
                if confirmation == "Y":
                    self.notes.remove(note)
                print (f"Note {note_id} has been deleted.")
                if confirmation == "N":
                    print ("Please check note ID or exit this action")
                return

                
#Method to save notes

    def save_notes_to_file(self):
        with open("notes.txt", "w" ) as file:
            for note in self.notes:
                file.write(f"ID: {note['ID']}\n")
                file.write(f"Title: {note['Title']}\n")
                file.write(f"Content: {note['Content']}\n")
                file.write("\n")


#Next is the method to load notes from files

    def load_notes_from_file(self):
        if os.path.isfile("notes.txt"):
            with open("notes.txt", "r") as file:
                lines = file.readlines()
                note_info = {}

            for line in lines:
                if line.strip() == "":
                    if note_info:
                        self.notes.append(note_info)
                        note_info = {}
                else:
                    key, value = line.strip().split(": ")
                    note_info[key.lower()] = value

           
            if note_info:
                self.notes.append(note_info)
        else:
            print("No notes found in file. Please create a new note.")



#Next is the method to be able to select actions amongst the notes

    def run(self):
        self.load_notes_from_file()
        while True:
            print("\n Welcome to your Notebook Menu! Please select any of the below options to continue or Exit:")
            print("1. Create a new note")
            print("2. View an existing note")
            print("3. Edit an existing note")
            print("4. Delete an existing note")
            print("5. Save Notes to a file")
            print("6. Exit Notebook")

            choice = input("Please enter the number of the action you would like to continue with:")


            if choice == '1':
                self.create_note()
            elif choice == '2':
                self.view_note()
            elif choice == '3' :
                self.edit_note()
            elif choice == '4':
                self.delete_note()
            elif choice == '5' :
                self.save_notes_to_file()
            elif choice == '6' :
                print("You are now exiting The Notebook. Thank you for visiting!")
                break
            else:
                print("Now that wasn't one of the options was it? Try again")



if __name__ == "__main__":
    notebook = Notebook()
    notebook.run()