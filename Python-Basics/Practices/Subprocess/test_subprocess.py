import subprocess

result = subprocess.run(["echo", "Welcome to India"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=TRUE)

print(result.stdout)
                        
#subprocess.run() - input

import subprocess
subprocess.run("python3", "add.py", text=TRUE, input ="2 3")
                        
#subprocess.Popen()
#wait

import subprocess
process = subprocess.Popen(["ls", "-la"])
process.wait()
print("completed")

#communicate - used to get the output, error and give input to the commannd.  

import subprocess

process = subprocess.run(["echo", "Welcome to India"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=TRUE)
result = process.communicate()
print(result.stdout)

#poll - check whether the exceution of the command is completed or not

import subprocess
process = subprocess.Popen(['ping', '-c 5', 'google.com'], stdout=subprocess.PIPE, text=TRUE)
while True:
    output = process.stdout.readline()
    if output:
        print(output.strip())
    result = process.poll()
    if result is not None:
        break


