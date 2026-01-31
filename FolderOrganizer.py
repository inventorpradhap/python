import os
import shutil
from pathlib import Path

def organize_files(folder_path):
    # Define extensions and their target folders
    categories = {
        'Music': ['mp3', 'aac', 'wav', 'mpeg'],
        'Images': ['jpeg', 'png', 'webp', 'jpg','jfif', 'gif'],
        'Videos' :['mp4', 'mkv','mov'],
        'Documents': ['doc', 'docx', 'pptx', 'pdf', 'xlsx', 'xlsm', 'txt','csv'],
        'SoftwareScrpts': ['py', 'm', 'c', 'cpp', 'slx', 'json'],
        'Software': ['exe', 'zip', 'msi','rar','jar','apk'],
        'PhotoShopfiles':['psd'],
        'Fonts' : ['ttf'],
        'Html': ['html','xml'],
        'Links': ['torrent','srt'],
        'Design files': ['stl', 'dxf']
    }
    
    folder = Path(folder_path)
    if not folder.exists():
        print(f"Folder '{folder_path}' does not exist.")
        return
    
    moved_count = 0
    for file_path in folder.iterdir():
        if file_path.is_dir():
            continue  # Skip subdirectories
        
        file_ext = file_path.suffix.lower().lstrip('.')
        target_folder = None
        
        for cat_folder, exts in categories.items():
            if file_ext in exts:
                target_folder = folder / cat_folder
                break
        
        if target_folder is None:
            continue  # Skip files not matching any category
        
        target_folder.mkdir(exist_ok=True)
        
        # Handle duplicates by appending (1), (2), etc.
        target_file = target_folder / file_path.name
        counter = 1
        while target_file.exists():
            name_without_ext = file_path.stem
            ext = file_path.suffix
            target_file = target_folder / f"{name_without_ext} ({counter}){ext}"
            counter += 1
        
        shutil.move(str(file_path), str(target_file))
        print(f"Moved '{file_path.name}' to '{target_folder}'")
        moved_count += 1
    
    print(f"Organized {moved_count} files.")

# Usage: Replace with your folder path
if __name__ == "__main__":
    organize_files(r"C:\Users\inven\Downloads")  # Use raw string for Windows paths
