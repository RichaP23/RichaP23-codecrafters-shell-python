import sys
import os
import subprocess
from pathlib import Path

def execute_command(command):
    """ Execute the command and handle output redirection. """
    if '>' in command:
        parts = command.split(">", 1)
        cmd_part = parts[0].strip()
        output_file = parts[1].strip()

        # Remove optional '1>' (which means stdout redirection)
        if output_file.startswith("1>"):
            output_file = output_file[2:].strip()

        try:
            # Execute command and capture output
            result = subprocess.run(cmd_part, shell=True, capture_output=True, text=True)
            
            # Write stdout to the file
            with open(output_file, "w") as f:
                f.write(result.stdout)

            # Print error messages (e.g., "file not found") to standard error
            if result.stderr:
                sys.stderr.write(result.stderr)
        
        except Exception as e:
            print(f"Error executing command: {e}")
    else:
        os.system(command)  # Run normally if no redirection

def main():
    while True:
        sys.stdout.write("$ ")
        command = input().strip()

        if command == "exit 0":
            exit(0)
        
        execute_command(command)  # Handle both normal and redirected commands

if __name__ == "__main__":
    main()
