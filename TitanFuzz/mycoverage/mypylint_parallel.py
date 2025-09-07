import os
import re
import subprocess
import concurrent.futures
from typing import List, Tuple

def run_pylint_on_file(file_path: str, output_file: str) -> None:
    try:
        result = subprocess.run(
            ['pylint', '--output-format=text', file_path],
            capture_output=True,
            text=True,
            check=False,
            timeout=3000  
        )
    except subprocess.TimeoutExpired:
        with open(output_file, 'a') as f:
            f.write(f"# {'=' * 30}\n")
            f.write(f"# Analysis for: {os.path.basename(file_path)}\n")
            f.write(f"# {'=' * 30}\n\n")
            f.write("# Pylint analysis timed out (over 5 minutes)\n\n\n")
        return
    except Exception as e:
        with open(output_file, 'a') as f:
            f.write(f"# {'=' * 30}\n")
            f.write(f"# Analysis for: {os.path.basename(file_path)}\n")
            f.write(f"# {'=' * 30}\n\n")
            f.write(f"# Error running pylint: {str(e)}\n\n\n")
        return

    with open(output_file, 'a') as f:
        f.write(f"# {'=' * 30}\n")
        f.write(f"# Analysis for: {os.path.basename(file_path)}\n")
        f.write(f"# {'=' * 30}\n\n")
        
        if result.stdout:
            f.write(result.stdout)
        
        if result.stderr:
            f.write("\n# Stderr:\n")
            f.write(result.stderr)
        
        f.write("\n\n\n")

def process_folder(folder_idx: int) -> None:

    folder_path = f"/home/yujunzhe/TitanFuzz/mycoverage/test_programs_starcoder3_10000/group_{folder_idx}"
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
            files.append((num, os.path.join(folder_path, filename)))
    
    files.sort(key=lambda x: x[0])
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        futures = [
            executor.submit(run_pylint_on_file, file_path, output_file)
            for _, file_path in files
        ]
        
        concurrent.futures.wait(futures)
    
    print(f"group_{folder_idx} processed successfully!")

def run_pylint_on_all_files():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = [executor.submit(process_folder, i) for i in range(0, 3)]
        
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result() 
            except Exception as e:
                print(f"Error processing folder: {e}")

if __name__ == "__main__":
    run_pylint_on_all_files()
    print("Pylint analysis completed!")