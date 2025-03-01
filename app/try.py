import subprocess
import os
built_inPath=subprocess.run(["which","coco"],capture_output=True,text=True,shell=True)
print(built_inPath.returncode)
print(built_inPath.stdout)
print(built_inPath.stderr)
a=os.system("which coco")
print(a)
built_inPath=subprocess.run(["which","cat"],capture_output=True,text=True,shell=True)
print(built_inPath.returncode)
print(built_inPath.stdout)
print(built_inPath.stderr)
a=os.system("which cat")
print(a)
