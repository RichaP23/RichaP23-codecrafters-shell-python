import sys
import os
import subprocess
def main():
    while(True):
        PATH=os.environ.get("PATH","")
        paths=PATH.split(":")
        print(paths)
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
                    executable_path = os.path.join(path, first_word)
                    if os.path.isfile(executable_path) and os.access(executable_path, os.X_OK):
                        found = True
                        try:
                            result = subprocess.run([executable_path] + arguments, capture_output=True, text=True)
                            print(result.stdout, end="")
                            print(result.stderr, end="") #print stderr as well.
                        except FileNotFoundError:
                            print(f"{first_word}: command not found")
                        break
                    else: 
                        print(f"{command}: command not found")
        
        



if __name__ == "__main__":
    main()
