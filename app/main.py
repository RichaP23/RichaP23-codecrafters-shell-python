import sys


def main():
    while(True):
        # Uncomment this block to pass the first stage
        sys.stdout.write("$ ")

        # Wait for user input
        command=input()
        if(command=="exit 0"):
            exit(0)
        first_word=command.split(" ",1)[0]
        if(first_word=="echo"):
            print(f"{command.split(" ",1)[1]}")
        else:
            print(f"{command}: command not found")



if __name__ == "__main__":
    main()
