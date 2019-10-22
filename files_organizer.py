import os
import mimetypes
import shutil
import folders_tree
import send2trash

def scan_folders():
    folder_to_track = folders_tree.folder_to_track()
    for folderName, subfolders, filenames in os.walk(folder_to_track):
        for filename in filenames:
            os.chdir(folderName)
            move_file()
            remove_empty_folders()
            
    

def remove_empty_folders():
    folder_to_track = folders_tree.folder_to_track()
    for folderName, subfolders, filenames in os.walk(folder_to_track):
        for subfolder in subfolders:
            try:
                subfolder = os.path.join(folderName, subfolder)
                list_of_files_in_subfolder = os.listdir(subfolder)
                number_of_files_in_subfolder = len(list_of_files_in_subfolder)
                if number_of_files_in_subfolder == 0:
                    try:
                        send2trash.send2trash(subfolder)
                    except:
                        pass
            except:
                pass
    


def move_file():
    extensions_folders = folders_tree.folders()
    folder_to_track = folders_tree.folder_to_track()
    for filename in os.listdir('.'):
        try:
            extension_of_file = str(os.path.splitext(folder_to_track + '/' + filename)[1])
            new_folder = extensions_folders[extension_of_file]
            if not os.path.exists(new_folder):
                os.makedirs(new_folder)
            shutil.move(filename, new_folder + '/' + filename)
        except Exception:
            extension_of_file = 'noname'



scan_folders()

