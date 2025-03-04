import subprocess
try: 
    str="which cat"
    built_inPath=subprocess.run(["ls","."],capture_output=True,text=True,check=True)
    print(built_inPath.stdout)
    built_inPath=subprocess.run(["which","horse"],capture_output=True,text=True,check=True)
except subprocess.CalledProcessError:
    print("horse not found")