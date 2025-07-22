import os
import subprocess

base_command = [
    "python3", 
    "run_torch.py", 
    "--input-dir=../starcoder-generated/torch-inductor-generated/step{}-3shot", 
    "--res-dir=_results-torch-titan"
]

for i in range(39, 101):
    command = [arg.format(i) if '{' in arg else arg for arg in base_command]
    
    print(f"Executing: {' '.join(command)}")
    
    result = subprocess.run(command, capture_output=True, text=True)
    
    print(result.stdout)
    
    if result.returncode != 0:
        print(f"Error executing command: {' '.join(command)}")
        print(result.stderr)