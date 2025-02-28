import sys
import os
import subprocess
from pathlib import Path
def iterSingleString(var):
    l=var.split(" ")
    singleStringElements=[i[1-len(i):-1] for i in l if i.startswith("'") and i.endswith("'")]
    return singleStringElements
def find_command(command):
    paths = os.environ.get('PATH') or ""    
    for path in map(lambda s: f"{s}/{command}", paths.split(":")):
        if Path(path).exists():
            return path
                    
    return None

def main():
    while(True):
        PATH=os.environ.get("PATH","")
        paths=PATH.split(":")
        # Uncomment this block to pass the first stage
        sys.stdout.write("$ ")
        # Wait for user input
        command=input()
        built_in={"exit","echo","type"}
        #checking for exit input by user
        if(command=="exit 0"):
            exit(0)
        #getting the first word usually command
        first_word=command.split(" ",1)[0]
        #checking for first word 
        match first_word:
            case "echo":
                words=iterSingleString(command.split(" ",1)[1])
                statement=' '.join(words)
                print(statement)
                command=first_word+" "+statement
                os.system(command)
            case "type":
                os.system(command)
            case "pwd":
                os.system("pwd")
            case "cat":
                words=iterSingleString(command.split(" ",1)[1])
                try: 
                    for files in words:
                        os.system(f"cat {files}",endswith=" ")
                except FileNotFoundError:
                    print(f"{first_word}: {dir}: No such file or directory")

            case "cd":
                #with path : 
                try: 
                    dir=command.split(" ",1)[1]
                    w=""
                    flag=False
                    for ch in dir:
                        w=""
                        if(ch=="."):
                            w+="."
                            continue
                        elif(w=="./"):
                            w=""
                            continue
                        elif(w=="../"):
                            os.chdir(os.pardir)
                            w=""
                        elif(ch=="~"):
                            #os.system("cd $HOME")
                            home=os.getenv("HOME")
                            os.chdir(home)
                            w=""
                        else:
                            w+="c"
                            flag=True
                    if(flag):
                        flag=False
                        os.chdir(dir)
                    
                except FileNotFoundError:
                    print(f"{first_word}: {dir}: No such file or directory")
            case _:
                found = False
                for path in paths:
                    #and os.access(executable_path, os.X_OK)
                    executable_path = path+"/"+first_word
                    pathExecutable=find_command(command.split(" ",1)[0])
                    if pathExecutable:
                        found = True
                        try:
                            
                            #os.system(pathExecutable+" "+command.split(" ",1)[1])
                            os.system(command)
                        except FileNotFoundError:
                            print(f"{first_word}: command not found")
                        break
                    else: 
                        
                        print(f"{command}: command not found")
                        break
        
        



if __name__ == "__main__":
    main()
