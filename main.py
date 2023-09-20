from database import display_entries
from file_organizer import organize_files
from input_handler import get_keyword_mapping

if __name__ == "__main__":
    '''
    Need to add: 
        x allow for user input for keyword mappings (perhaps one day automatic detection)
        - allow user to search database 
        - detect differences other than filename? (type)
        - how to detect start with integer? ie 01-BinarySearch 02-HeapSort => Lecture Folder
    '''
    print("Welcome to OrganizeMe!")
    root_folder = input("First, enter the name of the folder you wish to organize: ")

    # keyword_mapping = {
    #     'Lectures': ['week'],
    #     'Exercises': ['exer'],
    #     'Practice Tests': ['practice', 'test'],
    # }
    keyword_mapping = get_keyword_mapping()

    organize_files(root_folder, keyword_mapping)
    #display_entries()
