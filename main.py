import os
import shutil
import time

# Set the download folder path
download_folder = 'C:\\Users\\Emmanuel Onyo\\Downloads'

days_threshold = 2
print("Reading your files >>>>>>>")
time.sleep(1)

# Create a new folder for the old files
new_folder = os.path.join(download_folder, 'OLD_FILES')
if not os.path.exists(str(new_folder)):
    os.mkdir(new_folder)

print("Creating a folder >>>>>>>")
time.sleep(1)
# Get the current timestamp
now = time.time()

filesfound = []
# Loop over all files in the download folder
for filename in os.listdir(download_folder):
    file_path = os.path.join(download_folder, filename)
    
    print("reading files >>>>>>>")
    print(filename)
    time.sleep(1)
    # Check if the file is older than the threshold
    if os.path.isfile(file_path) and (now - os.path.getmtime(file_path)) > (days_threshold * 86400):
        
        # Move the old file to the new folder
        print("Moving files >>>>>>>")
        print(filename)
        filesfound.append(filename)
        time.sleep(1)

        new_file_path = os.path.join(new_folder, filename)
        shutil.move(file_path, new_folder)

print("Operation Complete >>>>>>>")
print(len(filesfound), "files have been moved to the old folder")
