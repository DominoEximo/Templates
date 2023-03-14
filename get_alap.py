

import os
import sys
import shutil

CWD = os.getcwd()


def create(ext):
    
    result = "alap." + ext
    
    dest = CWD + "\\" + result

    if os.path.isfile(dest):
        print("The file already exists.")
        return 1
    else:
        shutil.copy(CWD + "\\"+ "templates"+ "\\" + "alap." + ext, dest)
        print("It has been done.")





def main():

    print("""---------------------------
Create an empty source file
---------------------------
1) Python [py]
2) C++    [cpp]
3) Java   [java]
q) quit""")

    while True:
        try:
            a = input("> ")
        except(EOFError, KeyboardInterrupt):
            print()
            a = "q"
        if a == "1":
            create("py")
            break
        elif a == "2":
            create("cpp")
            break
        elif a == "3":
            create("java")
            break
        elif a == "q":
            print("No file was created.")
            break
        else:
            print("Please choose from 1 to 3")
    
    print(CWD)




    



if __name__ == "__main__":
    main()