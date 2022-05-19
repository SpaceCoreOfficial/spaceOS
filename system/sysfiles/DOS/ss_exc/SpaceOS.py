import os, time
import os.path
import configparser
from colorama import init
from colorama import Back
init(autoreset=True)
#                                                                                                                            ================
#                                                                                                                            Hello from 2022!
#                                                                                                                            ================ 


#                                                                                                               /=========================================\
#                                                                                                              |-----------Errors and functions------------|
#                                                                                                              |  This code part include errors protocols  |
#                                                                                                               \=========================================/

os.system(command='title SpaceOS 4.7')
def wrong_command():
    print(Back.RED + user + ' | Wrong command error! [WrongCommandError]')

def CatalogError():
    print(Back.RED + var + " | chctl error! [CatalogError]")

def CtlgdlError():
    print(Back.RED + var + " | Deletecatalog error! [CtlgdlError]")

def clear():
    os.system(command='cls')

def DirectoryNotFoundError():
    print(Back.RED + var + " | Directory not found [DirectoryNotFoundError]")

def CatalogNameError():
    print(Back.RED + user + " | Working with catalog error [CatalogNameError]")

def SysCatalog():
    print(Back.RED + "You can't remove this catalog")

def ReadError():
    print(Back.RED + var + " | File reading error [ReadError]")



os.chdir("..")



clear()
print(Back.GREEN + "Starting...")
time.sleep(1)
clear()


#                                                                                                                 /===============================================\
#                                                                                                                |-------------------- Moving -------------------- |
#                                                                                                                |  In this function system, go up 2 directories   |
#                                                                                                                |------------------------------------------------ |
#                                                                                                                 \===============================================/

os.chdir('..')
os.chdir('..')
os.chdir('..')

print("Welcome to SpaceOS 4.7")
print("Enter the HELP command for help")


while True:
    user = input("$:")


#                                                                                                          /=================================================================\
#                                                                                                         |------------------------------ Help -------------------------------|
#                                                                                                         |                Here's the command output function                 |
#                                                                                                         |-------------------------------------------------------------------|
#                                                                                                          \=================================================================/


    if user == 'help':
        print(Back.YELLOW + '==========================================')
        print(Back.YELLOW + "---------Welcome to SpaceOS 4.7-----------")
        print(Back.YELLOW + '==========================================')
        print("\n|-------------------------------------------------|")
        print("|HELP to help                                     |")
        print("|PRINT or ECHO to output anything text            |")
        print("|CTL to view the current directory                |")
        print("|CHCTL to change the current directory            |")
        print("|CLEAR to clear screen                            |")
        print("|SYSINFO to show system info on this PC           |")
        print("|CRCTL to create folder                           |")
        print("|RMCTL to remove folder                           |")
        print("|FILE to open text editor                         |")
        print("|SpaceOS to display system information            |")
        print("|Tipe to display the contents of the file         |")
        print("|-------------------------------------------------|\n")


#                                                                                                          /=================================================================\
#                                                                                                         |----------------------------- Output ------------------------------|
#                                                                                                         |                  These are simple output commands                 |
#                                                                                                         |-------------------------------------------------------------------|
#                                                                                                          \=================================================================/


    elif user == 'print':
        var = input("print $:")
        print(var)

    elif user == 'echo':
        var = input("echo $:")
        print(var)


#                                                                        /========================================================================================================================\
#                                                                       |-------------------------------------------------------- Catalog ---------------------------------------------------------|
#                                                                       |               I came up with the CTL command by accident when I was reading about Steve Jobs and Apple-DOS               |
#                                                                       |--------------------------------------------------------------------------------------------------------------------------|
#                                                                        \========================================================================================================================/


    elif user == 'ctl':
        os.system(command='dir')

    elif user == 'clear':
        clear()

    elif user == 'sysinfo':
        os.system(command='systeminfo')

    elif user == 'chctl':
        var = input("chctl $:")
        try:
            os.chdir(var)
        except  FileNotFoundError:
                DirectoryNotFoundError()
    elif user == 'crctl':
        var = input("catalog name $:")
        try:
            os.mkdir(var)
        except:
            DirectoryNotFoundError()

    elif user == 'rmctl':
        var = input("catalog name $:")
        print("Are you sure you remove catalog: " + var + " [y/n]?")
        var1 = input("$:")
        if var == 'other':
            SysCatalog()
        elif var == 'system':
            SysCatalog()
        elif var == 'sprite':
            SysCatalog()
        elif var == 'user':
            SysCatalog()
        elif var == 'sysfiles':
            SysCatalog()
        elif var == '5474767491788774':
            DirectoryNotFoundError()
        elif var1 == 'y':
            try:
                os.rmdir(var)
            except:
                DirectoryNotFoundError()
        else:
            print("Catalog removing stopped")

    elif user == 'file':
        import tkinter
        from tkinter.filedialog import asksaveasfile, askopenfile
        from tkinter.messagebox import showerror
         
        FILE_NAME = tkinter.NONE
         
         
        def new_file():
            global FILE_NAME
            FILE_NAME = "Untitled"
            text.delete('1.0', tkinter.END)
         
         
        def save_file():
            data = text.get('1.0', tkinter.END)
            out = open(FILE_NAME, 'w')
            out.write(data)
            out.close()
         
         
        def save_as():
            out = asksaveasfile(mode='w', defaultextension='.txt')
            data = text.get('1.0', tkinter.END)
            try:
                out.write(data.rstrip())
            except Exception:
                showerror(title="Oops!", message="Unable to save file....")
         
         
        def open_file():
            global FILE_NAME
            inp = askopenfile(mode="r")
            if inp is None:
                return
            FILE_NAME = inp.name
         
            data = inp.read()
            text.delete('1.0', tkinter.END)
            text.insert('1.0', data)
         
        root = tkinter.Tk()
        root.title("SpacePAD v0.1b")
        root.minsize(width=400, height=400)
        root.maxsize(width=400, height=400)
         
        text = tkinter.Text(root, width=400, height=400)
        text.pack()
         
        menuBar = tkinter.Menu(root)
        fileMenu = tkinter.Menu(menuBar)
        fileMenu.add_command(label="New", command=new_file)
        fileMenu.add_command(label="Open", command=open_file)
        fileMenu.add_command(label="Save", command=save_file)
        fileMenu.add_command(label="Save As", command=save_as)
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=root.quit)
        menuBar.add_cascade(label="File", menu=fileMenu)
         
        root.config(menu=menuBar)
        root.mainloop()
        file.close()

    elif user == 'SpaceOS':
        print("\n------------------------------------------------------------------------------------------------------------------------\nSpaceOS (powered by Windows)\nSystem version: 4.7\nMade by Space Core (My steam: 1144347594, My discord: Space Core#8097)\nOur discord server - https://discord.gg/TdTuqtuCq2\n------------------------------------------------------------------------------------------------------------------------\n")


    elif user == 'type':
        var = input("Filename $:")
        try:
            f = open(var, 'r')
            print(f.read())
            f.close()
        except:
            ReadError()



    else:
        wrong_command()