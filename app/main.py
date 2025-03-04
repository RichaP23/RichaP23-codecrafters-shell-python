import sys
import os
import subprocess
from pathlib import Path
def checkRedirect(command):
    try:
        if(command.split(" ")[2]==">" or command.split(" ")[2]=="1>"):
            return True
    except IndexError:
        return False
    return False
def redirectToFile(command,cout):
    if(checkRedirect(command)):
        try:
            file=command.split(" ")[3]
            fptr=fopen(file,"w")
            file.write(cout.stdout)
        except IndexError:
            print(cout.stdout)
    else:
        print(cout.stdout)
def quotedText(text):
    textList=[]
    word=""
    openQuote=False
    for i in text : 
        #this is the start quote
        if((i=="'" or i=='"') and openQuote==False):
            openQuote=True
            quote=i
            continue
        #if quote is already opened : 
        elif((i=="'" or i=='"') and openQuote==True):
            if(i==quote):
                textList.append(word.strip())
                lastquote=quote
                quote=""
                word=""
                openQuote=False
                continue
            else: 
                word +=i  # Add backslash before the quote
        else:
            word+=i
    return textList,lastquote
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
                cout=subprocess.run([command],capture_output=True,text=True)
                redirectToFile(command,cout)
            case "type":
                cout=subprocess.run([command],capture_output=True,text=True)
                redirectToFile(command,cout)
            case "pwd":
                cout=subprocess.run(["pwd"],capture_output=True,text=True)
                redirectToFile(command,cout)
            case "cat":
                words,quote=quotedText(command.split(" ",1)[1])
                try: 
                    for files in words:
                        if(quote=='"'):
                            cout=subprocess.run(["cat",f"\"{files}\""],capture_output=True,text=True)
                        else:
                            cout=subprocess.run(["cat",f"\"{files}\""],capture_output=True,text=True)
                        redirectToFile(command,cout)
                        
                except FileNotFoundError:
                    print(f"{first_word}: {files}: No such file or directory")
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
                built_inPath=subprocess.run(["which",first_word],capture_output=True,text=True)
                for path in paths:
                    #and os.access(executable_path, os.X_OK)
                    executable_path = path+"/"+first_word
                    pathExecutable=find_command(command.split(" ",1)[0])
                    if pathExecutable:
                        found = True
                        try:
                            os.system(command)
                        except FileNotFoundError:
                            print(f"{first_word}: command not found")
                        break
                    elif(built_inPath!=f"{first_word} not found"):
                        '''if(first_word.startswith("invalid")):
                                print(f"{command}: command not found")
                            #os.system(pathExecutable+" "+command.split(" ",1)[1])
                        else:
                            os.system(command)'''
                        textList,quote=quotedText(command)
                        try:
                            built_inPath=subprocess.run(textList,capture_output=True,text=True,check=True)
                            print(built_inPath.stdout)
                        except subprocess.CalledProcessError:
                            print(f"{command}: command not found")
                        break
                    else: 
                        print(f"{command}: command not found")
                        break

        
        



if __name__ == "__main__":
    main()
