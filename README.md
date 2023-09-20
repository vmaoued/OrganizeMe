# OrganizeMe

OrganizeMe is a file organization application initially tailored for university students and professors but offers a universal solution to streamline the management of multiple files.
The application provides dynamic sorting of files based on user-defined keyword mappings, combined with SQLite integration for detailed file tracking.

## Features
- **Dynamic File Sorting**: Sorts files in a given directory into organized sub-folders. Allows users to define their own keyword mappings, enabling the system to organize files based on individual needs.
- **SQLite Integration**: Uses SQLAlchemy for efficient file tracking and offers user-defined searches for ease of file discovery.

## Demo
Here's an example of how OrganizeMe works. Let's organize this CMPUT 204 folder with the keywords: Lectures, Exercises, and Practice Tests.
Here is CMPUT 204 before:

<img width="248" alt="before_sort_v1" src="https://github.com/vmaoued/OrganizeMe/assets/114374462/46eb3d3e-0232-4f22-9c8a-6d0921d42f51">


We run the following:

<img width="698" alt="terminal" src="https://github.com/vmaoued/OrganizeMe/assets/114374462/e7462400-c173-4816-a401-7379db2a8d7a">


And observe the changes in the CMPUT 204 folder:

<img width="269" alt="after_sort_v1" src="https://github.com/vmaoued/OrganizeMe/assets/114374462/c3fe674b-be8f-494c-bbb3-867fa012270b">


Where we have a folder for each of the keywords we inputted, along with the "Others" folder that is automatically generated for any files not matching the inputted keys.

<img width="267" alt="after_sort_v1 1" src="https://github.com/vmaoued/OrganizeMe/assets/114374462/9c9ca131-e22e-45ee-9046-3871624a5c4c">


All files are now sorted to our liking for easy access.

`courses.db` is also updated to hold all the file names and relevant information for each file, which we can individually explore.

## Installation

1. Ensure you have Python installed.
2. Clone the repository:
`git clone https://github.com/vmaoued/OrganizeMe.git`
3. Navigate to the directory and install the required packages:
`pip install -r requirements.txt`

## Usage
1. Copy/move the folder you wish to organize into the working directory.
2. Run the main script:
`python main.py`
3. Follow the prompts on screen to customize how you would like your folder to be organized, or explore the SQLite database for more info on your files.
