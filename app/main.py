import sys
import os
import subprocess
from pathlib import Path

def quotedText(text):
    textList = []
    word = ""
    lastquote = ""
    openQuote = False
    for i in text:
        if (i == "'" or i == '"') and openQuote == False:
            openQuote = True
            quote = i
            continue
        elif (i == "'" or i == '"') and openQuote == True:
            if i == quote:
                textList.append(word.strip())
                lastquote = quote
                quote = ""
                word = ""
                openQuote = False
                continue
            else:
                word += i
        else:
            word += i
    return textList, lastquote

def find_command(command):
    paths = os.environ.get('PATH') or ""
    for path in map(lambda s: f"{s}/{command}", paths.split(":")):
        if Path(path).exists():
            return path
    return None

def execute_command(command):
    parts = command.split(" ", 1)
    if len(parts) > 1:
        cmd, rest = parts
        redirect_parts = rest.split(">", 1)
        if len(redirect_parts) > 1:
            command_args, output_file = redirect_parts
            output_file = output_file.strip()
            command_args = command_args.strip()
            try:
                result = subprocess.run(command_args.split(), capture_output=True, text=True, check=False)
                with open(output_file, "w") as f:
                    f.write(result.stdout)
                if result.stderr:
                    sys.stderr.write(result.stderr)

            except FileNotFoundError:
                print(f"{cmd}: command not found")
            except Exception as e:
                print(f"Error: {e}")
            return True
        else:
            try:
                subprocess.run(command.split(), check=False)
                return True
            except FileNotFoundError:
                print(f"{cmd}: command not found")
            except Exception as e:
                print(f"Error: {e}")
            return True

    else:
        try:
            subprocess.run(command.split(), check=False)
            return True
        except FileNotFoundError:
            print(f"{command}: command not found")
        except Exception as e:
            print(f"Error: {e}")
        return True

def main():
    while True:
        sys.stdout.write("$ ")
        command = input()
        if command == "exit 0":
            exit(0)
        execute_command(command)

if __name__ == "__main__":
    main()