from database import display_entries
from file_organizer import organize_files

if __name__ == "__main__":
    root_folder = input("Enter root folder (e.g., Math 241): ")
    keyword_mapping = {
        'Lectures': ['week'],
        'Exercises': ['exer'],
        'Practice Tests': ['practice', 'test'],
    }

    organize_files(root_folder, keyword_mapping)
    #display_entries()
