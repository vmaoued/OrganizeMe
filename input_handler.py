# keyword_mapping = {
#     'Lectures': ['week'],
#     'Exercises': ['exer'],
#     'Practice Tests': ['practice', 'test'],
# }

def get_keyword_mapping():
    print("Next, indicate the folder names (followed by its respective identifying keyword(s)) you wish to have you files organized into.")
    mapping = {}
    while True:
        folder_name = input("Enter the folder name or 'done' to finish: ")
        if folder_name.lower() == 'done':
            break
        keywords = input(f"Enter keywords for {folder_name} separated by commas: ").split(',')
        keywords = [k.strip() for k in keywords] 
        mapping[folder_name] = keywords
    return mapping
