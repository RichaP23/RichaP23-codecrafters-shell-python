import sys
import os
import subprocess
from pathlib import Path
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
                print(f"{command.split(" ",1)[1]}")
            case "type":
                subprocess.run("type "+command.split(" ",1)[1])
            case _:
                found = False
                for path in paths:
                    #and os.access(executable_path, os.X_OK)
                    executable_path = path+"/"+first_word
                    if find_command("custom_exe_1234"):
                        found = True
                        try:
                            result = subprocess.run("cd"+executable_path)
                            resultFinal=subprocess.run("./"+command.split(" ",1)[1])
                            print(resultFinal.stdout, end="")
                            print(result.stderr, end="") #print stderr as well.
                        except FileNotFoundError:
                            print(f"{first_word}: command not found entering file check look but not finding path")
                        break
                    else: 
                        print(f"{command}: command not found its not entering file check loop")
        
        



if __name__ == "__main__":
    main()
