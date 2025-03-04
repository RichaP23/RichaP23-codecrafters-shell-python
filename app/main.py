import sys
import os
import subprocess
from pathlib import Path

def find_command(command):
    paths = os.environ.get('PATH', '').split(':')
    for path in paths:
        executable_path = Path(path) / command
        if executable_path.exists() and os.access(executable_path, os.X_OK):
            return str(executable_path)
    return None

def execute_command(command):
    parts = command.split(">", 1)
    if len(parts) > 1:
        cmd_part = parts[0].strip()
        output_file = parts[1].strip()

        cmd_parts = cmd_part.split()
        if cmd_parts:
            cmd = cmd_parts[0]
            args = cmd_parts[1:]

            if cmd == "echo":
                # Special handling for echo
                output = " ".join(args)
                with open(output_file, "w") as f:
                    f.write(output)
                return True

            cmd_path = find_command(cmd)
            if cmd_path:
                try:
                    result = subprocess.run([cmd_path] + args, capture_output=True, text=True, check=False)
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
                print(f"{cmd}: command not found")
                return True
    else:
        cmd_parts = command.split()
        if cmd_parts:
            cmd = cmd_parts[0]
            args = cmd_parts[1:]
            cmd_path = find_command(cmd)
            if cmd_path:
                try:
                    subprocess.run([cmd_path] + args, check=False)
                    return True
                except FileNotFoundError:
                    print(f"{cmd}: command not found")
                except Exception as e:
                    print(f"Error: {e}")
                return True
            else:
                print(f"{cmd}: command not found")
                return True
        else:
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