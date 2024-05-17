import os
import shutil

# Function to organize files by their types into separate folders
def organize_files(directory):
    # Dictionary to store file types and their corresponding folders
    file_types = {
        'Documents': ['.pdf', '.doc', '.docx', '.txt'],
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Videos': ['.mp4', '.mov', '.avi'],
        'Audios': ['.mp3', '.wav'],
        'Archives': ['.zip', '.rar', '.tar', '.gz'],
        'Executables': ['.exe', '.msi']
    }

    # Create folders if they don't exist
    for folder in file_types:
        folder_path = os.path.join(directory, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # Organize files into respective folders
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1]
            for file_type, extensions in file_types.items():
                if file_extension in extensions:
                    destination_folder = os.path.join(directory, file_type)
                    shutil.move(file_path, destination_folder)
                    print(f"Moved '{filename}' to '{file_type}' folder.")
                    break

# Main function to run the script
def main():
    directory = input("Enter the directory path to organize files: ")
    organize_files(directory)
    print("File organization completed!")

if __name__ == "__main__":
    main()
