import sys
import os
import subprocess
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
                    if os.path.isfile(executable_path):
                        found = True
                        try:
                            result = subprocess.run(path+"/"+command)
                            print(path+"/"+command)
                            print(result.stdout, end="")
                            print(result.stderr, end="") #print stderr as well.
                        except FileNotFoundError:
                            print(f"{first_word}: command not found entering file check look but not finding path")
                        break
                    else: 
                        print(f"{command}: command not found its not entering file check loop")
        
        



if __name__ == "__main__":
    main()
