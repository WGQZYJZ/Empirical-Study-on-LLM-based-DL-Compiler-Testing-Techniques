import os
import re

def calculate_generation_time(main_dir):
    total_time = 0.0
    pattern = re.compile(r'@Generation:\s*(\d+\.?\d*)s')
    processed_files = 0
    errors = 0

    for entry in os.listdir(main_dir):
        dir_path = os.path.join(main_dir, entry)
        if not os.path.isdir(dir_path):
            continue

        log_file = os.path.join(dir_path, 'model_gen.log')
        if not os.path.isfile(log_file):
            print(f"Error: model_gen.log not found in directory {entry}")
            errors += 1
            continue

        try:
            with open(log_file, 'r') as f:
                lines = f.readlines()
                last_line = None
                for line in reversed(lines):
                    if line.strip():
                        last_line = line.strip()
                        break

                if not last_line:
                    print(f"The file {log_file} is empty")
                    errors += 1
                    continue

                match = pattern.search(last_line)
                if match:
                    time_value = float(match.group(1))
                    total_time += time_value
                    processed_files += 1
                else:
                    print(f"Error: Last line of file {log_file} does not match format: {last_line}")
                    errors += 1

        except Exception as e:
            print(f"Error processing file {log_file} : {str(e)}")
            errors += 1

    print("\Statistical results:")
    print(f"Number of files processed successfully: {processed_files}")
    print(f"Number of errors/failed files: {errors}")
    print(f"Total Generation time: {total_time:.4f} seconds")
    return total_time

if __name__ == "__main__":
    target_dir = "/home/yujunzhe/nnsmith/outputs/2025-04-16/"
    if not os.path.exists(target_dir):
        print(f"The directory {target_dir} does not exist")
    elif not os.path.isdir(target_dir):
        print(f"{target_dir} is not a directory")
    else:
        calculate_generation_time(target_dir)