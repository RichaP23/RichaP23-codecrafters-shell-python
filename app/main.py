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
    parts = command.split(" ", 1)
    if len(parts) > 0:
        cmd_part = parts[0]
        if len(parts) > 1:
            rest = parts[1]
            redirect_parts = rest.split(">", 1)
            if len(redirect_parts) > 1:
                command_args, output_file = redirect_parts
                output_file = output_file.strip()
                command_args = command_args.strip()
                cmd_path = find_command(cmd_part)
                if cmd_path:
                    try:
                        result = subprocess.run([cmd_path] + command_args.split(), capture_output=True, text=True, check=False)
                        with open(output_file, "w") as f:
                            f.write(result.stdout)
                        if result.stderr:
                            sys.stderr.write(result.stderr)
                    except FileNotFoundError:
                        print(f"{cmd_part}: command not found")
                    except Exception as e:
                        print(f"Error: {e}")
                    return True
                else:
                    print(f"{cmd_part}: command not found")
                    return True

            else:
                cmd_path = find_command(cmd_part)
                if cmd_path:
                    try:
                        subprocess.run([cmd_path] + redirect_parts[0].split(), check=False)
                        return True
                    except FileNotFoundError:
                        print(f"{cmd_part}: command not found")
                    except Exception as e:
                        print(f"Error: {e}")
                    return True
                else:
                    print(f"{cmd_part}: command not found")
                    return True
        else:
            cmd_path = find_command(cmd_part)
            if cmd_path:
                try:
                    subprocess.run([cmd_path], check=False)
                    return True
                except FileNotFoundError:
                    print(f"{cmd_part}: command not found")
                except Exception as e:
                    print(f"Error: {e}")
                else:
                    print(f"{cmd_part}: command not found")
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