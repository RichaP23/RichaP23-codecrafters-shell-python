import sys
import os
def main():
    while(True):
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
                os.system("type "+command.split(" ",1)[1])
            case _:
                #checking for env variable 
                envCheckCommand="echo $"+first_word.upper
                envCheck=os.system(envCheckCommand)
                if(envCheck!=0):
                    os.system(command)
                else: 
                    print(f"{command}: command not found")
    
        



if __name__ == "__main__":
    main()
