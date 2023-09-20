from database import display_entries, search_entries
from file_organizer import organize_files
from input_handler import get_keyword_mapping

if __name__ == "__main__":
    '''
    Need to add: 
        x allow for user input for keyword mappings (perhaps one day automatic detection)
        x allow user to search database 
        - detect differences other than filename? (type)
        - how to detect start with integer? ie 01-BinarySearch 02-HeapSort => Lecture Folder
    '''
    print("Welcome to OrganizeMe!")
    done = False

    while not done:

        print("What would you like to do today?\n 1. Organize a folder \n 2. Browse your files \n 3. Exit")
        option = input()

        if option == '1':
            root_folder = input("First, enter the name of the folder you wish to organize: ")

            keyword_mapping = get_keyword_mapping()

            organize_files(root_folder, keyword_mapping)
   
            print(f"{root_folder} is now organized just how you like it!")

            cont = input("Would you like to continue? Y/N: ")
            if cont.lower() == 'n':
                done = True
        
        elif option == '2':
            print("Now browsing the database, would you like to: \n 1. Search with keywords \n 2. Display the whole database \n 3. Exit")
            select = input()

            if select == "3":
                break
            elif select == "2":
                display_entries()
            elif select == "1":
                keywords = input("Enter keywords: ")
                search_entries(keywords)

            cont = input("Would you like to continue? Y/N: ")
            if cont.lower() == 'n':
                done = True
            
        elif option == '3':
            done = True
        
        else:
            print("Please enter a valid input")

    print("Thanks for using OrganizeMe. See you again!")