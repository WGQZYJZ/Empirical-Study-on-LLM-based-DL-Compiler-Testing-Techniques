import os
import subprocess

def run_pylint_on_all_files():
    folder_path = "test_progarms_whitefox_all"
    output_file = os.path.join(folder_path, "pylint.txt")
    
    if not os.path.exists(folder_path):
        print(f"Error: Folder '{folder_path}' does not exist!")
        return
        
    # open(output_file, 'w').close()

    for num in range(10001, 12201):
        filename = f"torch{num}.py"
        file_path = os.path.join(folder_path, filename)
        

        if not os.path.exists(file_path):
            with open(output_file, 'a') as f:
                f.write(f"# File not found: {filename}\n\n")
            continue

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
    print("Success! ")