import sys
import os
import subprocess

def execute_command(command):
    """ Execute the command and handle output redirection properly. """
    if '1>' in command : 
        output_file = output_file[2:].strip()
    elif '>' in command:
        parts = command.split(">", 1)
        cmd_part = parts[0].strip()
        output_file = parts[1].strip()

        try:
            # Execute command and capture output
            result = subprocess.run(cmd_part, shell=True, capture_output=True, text=True)
            
            # Write only stdout to the file without extra characters
            with open(output_file, "w") as f:
                f.write(result.stdout.rstrip() + "\n")  # Ensure proper newline formatting

            # Print errors (stderr) to console if any
            if result.stderr:
                sys.stderr.write(result.stderr)
        
        except Exception as e:
            print(f"Error executing command: {e}")
    else:
        os.system(command)  # Run normally if no redirection

def main():
    while True:
        sys.stdout.write("$ ")  # Prompt before taking input
        sys.stdout.flush()  # Ensure it appears immediately
        
        command = input().strip()  # Read user input

        if command == "exit 0":
            exit(0)
        
        execute_command(command)  # Handle both normal and redirected commands

if __name__ == "__main__":
    main()
