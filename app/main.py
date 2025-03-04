import sys
import os
import subprocess

def execute_command(command):
    """ Execute the command and handle output redirection properly. """
    if '>' in command:
        parts = command.split(">", 1)
        cmd_part = parts[0].strip()
        output_file = parts[1].strip()

        # Remove '1>' explicitly if present
        if output_file.startswith("1>"):
            output_file = output_file[2:].strip()

        try:
            # Execute command and capture output
            result = subprocess.run(cmd_part, shell=True, capture_output=True, text=True)
            
            # Write only stdout to the file, without extra numbers
            with open(output_file, "w") as f:
                f.write(result.stdout.rstrip())  # Use rstrip() to avoid extra newlines or spaces

            # Print errors (stderr) to console if any
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
