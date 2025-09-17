import subprocess

# Basic command execution
result = subprocess.run(['ls', '-l'], capture_output=True, text=True)
print(result.returncode) # Exit status
print(result.stdout) # Standard output
print(result.stderr) # Standard error
# With shell expansion
result = subprocess.run('echo $HOME', shell=True, capture_output=True, text=True)
# Check for errors (raises CalledProcessError if returncode  0)
try:
    result = subprocess.run(['false'], check=True, capture_output=True, text=True)
except subprocess.CalledProcessError as e:
    print(f"Command failed with exit code {e.returncode}")

# Using Popen for more control
process = subprocess.Popen(['python', 'script.py'],
stdin=subprocess.PIPE,
stdout=subprocess.PIPE,
stderr=subprocess.PIPE,
text=True)
stdout, stderr = process.communicate(input='some input')
returncode = process.wait()

# Real-time output processing
process = subprocess.Popen(['tail', '-f', 'logfile.txt'],
stdout=subprocess.PIPE,
text=True)
for line in process.stdout:
    print(f"LOG: {line.strip()}")
    if 'ERROR' in line:
        process.terminate() # Stop the process