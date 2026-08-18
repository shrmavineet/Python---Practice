from pathlib import Path
import os

def readfileandfolder():
    path = Path('fileHandlingProject')
    items = list(path.rglob('*'))

    for i, items in enumerate(items):
        print(f"{i+1} : {items}")
def readfile():
    try:
        readfileandfolder()
        name = input("Which file you want to read: ")
        basepath = Path("fileHandlingProject")
        p = basepath / name
        if p.exists() and p.is_file():
            with open(p,'r') as fs:
                data = fs.read()
                print(data)
            print("Readed Successfully")
        else:
            print("The file doesnot exist")
    except Exception as err:
        print(f"An error occured as {err}")


def createfile():
    try:
        readfileandfolder()
        name = input("please tell your file name: ")
        basepath = Path("fileHandlingProject")
        p = basepath / name
        if not p.exists():
            with open(p, "w") as fs:
                data = input("what you want to write int his file: ")
                fs.write(data)
            print(f"FILE CREATED SUCCESSFULLY")
        else:
            print(f"File already exists")
    except Exception as err:
        print(f"An error occured as {err}")

def updatefile():
    try:
        readfileandfolder()
        name = input("Which file you want to update: ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("Press 1 for change the name of File")
            print("Press 2 for Overwriting the data of the file")
            print("Press 3 for appending some content in your file")

            res = int(input("enter your response: "))

            if res == 1:
                name2 = input("Tell your new file name: ")

                p2 = Path(name2)
                p.rename(p2)

            if res == 2:
                with open(p, 'w') as fs:
                    data = input("Tell what you want to write this will overwrite the data: ")
                    fs.write(data)
            if res == 3:
                with open(p, 'a') as fs:
                    data = input("Tell what you want to write this will overwrite the data: ")
                    fs.write(" "+data)
    except Exception as err:
        print(f"An occurend as {err}")

def deletefile():
    try:
        readfileandfolder()
        name = input("which file you want to delete: ")
        basepath = Path("fileHandlingProject")
        p = basepath / name

        if p.exists() and p.is_file():
            os.remove(p)

            print("file remove successfully")

        else:
            print("No such a file")
    except Exception as err:
        print(f"An error occured as {err}")


print("press 1 for Creating a file")
print("press 2 for Reading a file")
print("press 3 for Updating a file")
print("press 4 for deletion a file")

check = int(input("Please tell your request: "))

if check == 1:
    createfile()
if check == 2:
    readfile()
if check == 3:
    updatefile()
if check == 4:
    deletefile()