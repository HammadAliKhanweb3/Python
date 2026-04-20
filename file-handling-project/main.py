from pathlib import Path 
import os

def readFileAndFolder():
    path = Path('')
    items = list(path.rglob('*')) 
    for i,item in enumerate(items):
        print(f"{i+1} : {item}")


def createFile():
    try:
        readFileAndFolder()
        name = input("Enter your file name :- ")
        p = Path(name)
        with open(p,"w") as fs:
            data = input("What you want to write in this file:-")
            fs.write(data)
        print(F"File Created Successfully")
    
    except Exception as err:
        print(f"An error occurred as {err}") 


def readFile():
    try:    
        readFileAndFolder()
        name = input("Which file you want :- ")
        p = Path(name)
        
        if p.exists and p.is_file():
            with open(p,"r") as fs:
                data = fs.read
                print(data)
            print(F"File Readed Successfully")
        else:
            print("the file doesnot exit")
    except Exception as err:
        print(f"An error occured as {err}")


def updateFile():
    try:
        readFileAndFolder()
        name = input("which file you want to update :-")
        p = Path(name)
        if p.exists and p.is_file:
            print("Press 1 to rename the file :-")
            print("Press 2 to update the file :-")
            print("Press 3 to append content in the file :-")
            
            response = int(input("Enter your response :-"))

            if response == 1:
                rename = input("Enter new file name :-")
                p2 = Path(rename)
                p.rename(p2)

            elif response == 2:
                with open(p,'w') as fs:
                    content = input("Enter content to update :-")
                    fs.write(content)
            
            elif response == 3:
                with open(p,"a") as fs:
                    content = input("Enter content to update :-")
                    fs.write(" "+content)
    except Exception as err:
         print(f"An error occured as {err}")    


            
def deleteFile():
    try:    
        readFileAndFolder()
        name = input("Which file you want delete:- ")
        p = Path(name)
        
        if p.exists and p.is_file():
            os.remove(name)
            print("File removed Successfully")

    except Exception as err:
        print(f"An error occured as {err}")
     
        

print("Press 1 to create a file")
print("Press 2 to read a file")
print("Press 3 to update a file")
print("Press 4 to delete a file")

check = int(input("please tell your response"))

if check == 1:
    createFile()
elif check == 2:
    readFile()
elif check == 3:
    updateFile()
elif check == 4:
    deleteFile()
