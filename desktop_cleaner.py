import os
import shutil


def move_desktop_files(destination_folder):
    desktop_path = os.path.join("C:", os.sep, "Users", "louay", "OneDrive", "Bureau")

    # Create the destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    print("Desktop folder created successfully!")
    # Iterate through files and folders on the desktop
    for item in os.listdir(desktop_path):
        item_path = os.path.join(desktop_path, item)

        # Check if the item is a file or directory (excluding shortcuts)
        if os.path.isfile(item_path) and (
            not item.endswith(".lnk") or not item.endswith(".url")
        ):
            # Move the file to the destination folder
            shutil.move(item_path, destination_folder)
        elif os.path.isdir(item_path) and not item.endswith(".lnk"):
            # Move the directory to the destination folder
            shutil.move(item_path, destination_folder)


if __name__ == "__main__":
    # Specify the destination folder where you want to move the files
    destination_folder = "C:\\Users\\louay\\OneDrive\\Documents\\desktop"
    move_desktop_files(destination_folder)
    print("Desktop files moved successfully!")
