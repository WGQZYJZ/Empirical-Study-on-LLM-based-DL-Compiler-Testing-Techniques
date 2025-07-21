import os
import re
import subprocess

def run_pylint_on_all_files():
    folder_path = "test_progarms_whitefox_1000"
    output_file = os.path.join(folder_path, "pylint.txt")
    
    if not os.path.exists(folder_path):
        print(f"Error: Folder '{folder_path}' does not exist!")
        return

    with open(output_file, 'w'):
        pass

    files = []
    for filename in os.listdir(folder_path):
        match = re.fullmatch(r'torch(\d+)\.py', filename)
        if match:
            num = int(match.group(1))
            files.append((num, filename))
    
    files.sort()

    for num, filename in files:
        file_path = os.path.join(folder_path, filename)
        
        try:
            result = subprocess.run(
                ['pylint', file_path],
                capture_output=True,
                text=True,
                check=False
            )
        except Exception as e:
            with open(output_file, 'a') as f:
                f.write(f"# Error running pylint on {filename}: {str(e)}\n\n")
            continue

        with open(output_file, 'a') as f:
            f.write(f"# {'=' * 30}\n")
            f.write(f"# Analysis for: {filename}\n")
            f.write(f"# {'=' * 30}\n\n")
            
            if result.stdout:
                f.write(result.stdout)
            
            if result.stderr:
                f.write("\n# Stderr:\n")
                f.write(result.stderr)
            
            f.write("\n\n\n")

if __name__ == "__main__":
    run_pylint_on_all_files()
    print("Pylint analysis completed!")