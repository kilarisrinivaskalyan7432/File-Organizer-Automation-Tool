import os
import shutil

def organize_files(folder_path):
    file_types = {
        "Images": [".jpg", ".png", ".jpeg"],
        "Documents": [".pdf", ".docx", ".txt"],
        "Videos": [".mp4", ".mkv"]
    }

    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)

        if os.path.isfile(file_path):
            for folder, extensions in file_types.items():
                if file.lower().endswith(tuple(extensions)):
                    
                    target_folder = os.path.join(folder_path, folder)

                    if not os.path.exists(target_folder):
                        os.makedirs(target_folder)

                    shutil.move(file_path, os.path.join(target_folder, file))
                    break

    print("Files organized successfully!")

# Run
path = input("Enter folder path: ")
organize_files(path)