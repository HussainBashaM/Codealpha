import os
import shutil

source_folder = input("Enter the source folder path: ").strip()
destination_folder = input("Enter the destination folder path: ").strip()

if not os.path.exists(source_folder):
    print("Source folder does not exist.")
    exit()

os.makedirs(destination_folder, exist_ok=True)

moved_files = 0

for filename in os.listdir(source_folder):
    if filename.lower().endswith(".jpg"):
        source_path = os.path.join(source_folder, filename)
        destination_path = os.path.join(destination_folder, filename)

        if os.path.isfile(source_path):
            shutil.move(source_path, destination_path)
            print(f"Moved: {filename}")
            moved_files += 1

print(f"\nFinished. {moved_files} JPG file(s) moved.")
