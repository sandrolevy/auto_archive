import os
import mimetypes
import shutil

def create_category_folders():
    os.chdir(folder_to_track)
    folders_to_create = [
        'Images', 'Video', 'Audio', 'Documents', 'Programs', 'Compressed',
        ]
    for folders in folders_to_create:
        if not os.path.exists(folders):
            os.makedirs(folders)

def scan_folders():
    os.chdir(folder_to_track)
    for root, dirs, files in os.walk("."):
        for name in files:
            print(os.path.join(root, name))
        for name in dirs:
            print(os.path.join(root, name))

def create_dicionary_of_extensions():
        mimetypes.init()
        general_type = [
            'image', 'video', 'audio', 'text',
        ]
        extensions = {}
        for type_of_file in general_type:
            extensions[type_of_file] = []            
            for ext in mimetypes.types_map:
                if mimetypes.types_map[ext].split('/')[0] == type_of_file:     
                    extensions[type_of_file].append(ext)           
        return extensions

def move_file():
    extensions = create_dicionary_of_extensions()
    images = extensions['image']
    video = extensions['video']
    audio = extensions['audio']
    for file in os.listdir(folder_to_track): 
        if any(file.endswith(ext) for ext in images):
            path = folder_to_track + '/' + 'Images'
            shutil.move(file, path + '/' + file)
        elif any(file.endswith(ext) for ext in video):
            path = folder_to_track + '/' + 'Video'
            shutil.move(file, path + '/' + file)
        elif any(file.endswith(ext) for ext in audio):
            path = folder_to_track + '/' + 'Audio'
            shutil.move(file, path + '/' + file)


folder_to_track = r'D:\Users\Levy\Downloads\Teste'
create_category_folders()
move_file()
