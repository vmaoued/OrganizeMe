import os
from database import add_entry_to_db

'''
Takes all files currently in given root folder and organizes them into folders based on 
the designated keyword mapping.
Input: root_folder, keyword_mapping
Output: None
'''
def organize_files(root_folder, keyword_mapping):

    all_files = set(os.listdir(root_folder))
   
    for filename in all_files.copy():
        matched = False
        for folder_name, keywords in keyword_mapping.items():
            for keyword in keywords:
                if keyword.lower() in filename.lower():
                    destination_folder = os.path.join(root_folder, folder_name)

                    if not os.path.exists(destination_folder):
                        os.makedirs(destination_folder)

                    src = os.path.join(root_folder, filename)
                    dest = os.path.join(destination_folder, filename)
                    os.rename(src, dest)

                    # database entry
                    add_entry_to_db(root_folder, folder_name, filename)

                    # remove from set and mark as matched
                    all_files.remove(filename)
                    matched = True
                    break

            if matched:
                break

    # handling unmatched files (move them to "Other" folder)
    for filename in all_files:
        other_folder = os.path.join(root_folder, "Other")
        if not os.path.exists(other_folder):
            os.makedirs(other_folder)

        src = os.path.join(root_folder, filename)
        dest = os.path.join(other_folder, filename)
        os.rename(src, dest)

        # database entry for the "Other" folder
        add_entry_to_db(root_folder, "Other", filename)
