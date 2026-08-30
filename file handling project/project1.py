from pathlib import Path
import os

def create_folder() :
    try :
        a=input("Please tell your folder name : ")
        p=Path(a)
        p.mkdir()
    except Exception as err :
        print("Error ocurred as ",err)



print("Options : ")
print("1. Create a folder")
print("2. Read files and folder")
print("3. Update the folder")
print("4. Delete the folder")
choice = int(input("Please choose options :"))

if choice==1 :
    create_folder()