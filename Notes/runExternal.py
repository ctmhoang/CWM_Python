import subprocess
completed = subprocess.run(["ls", "-l"],capture_output = True, text =True, check = True)
#completed = subprocess.run(["python3", "other.py"],capture_output = True, text =True)

print(type(completed))
print(completed.returncode) #if check
print(completed.stderr) 
print(completed.stdout)

#subprocess.call
#subprocess.check_call
#subprocess.check_output
#subprocess.Popen
