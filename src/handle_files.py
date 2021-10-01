import os
import shutil

# CREATE DIRECTORY
def create_directory(dirname:str):
    if dirname not in os.listdir():
        os.mkdir(dirname)
    else:
        print(f"directory {dirname} already exist")

# DELETE DIRECTORY
def delete_directory(dirname:str):
    if dirname in os.listdir():
        shutil.rmtree(dirname)
    else:
        print(f"Directory {dirname} not found")

# RENAME DIRECTORY
def rename_directory(oldname:str, newname:str):
    if oldname in os.listdir():
        os.rename(oldname, newname)
    else:
        print(f"Directory {oldname} not found")

# CREATE FILE
def create_file(filename:str):
    if filename not in os.listdir():
        file = open(filename,'w')
        file.close()
    else:
        print(f"File {filename} already exist")

# DELETE FILE
def delete_file(filename:str):
    if filename in os.listdir():
        os.remove(filename)
    else:
        print(f"File {filename} not found")

# RENAME FILE
def rename_file(oldname:str, newname:str):
    if oldname in os.listdir():
        os.rename(oldname, newname)
    else:
        print(f"File {oldname} not found")

delete_directory("checkfol")