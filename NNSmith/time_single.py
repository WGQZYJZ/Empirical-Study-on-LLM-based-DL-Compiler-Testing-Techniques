import os
import re

def main():
    base_dir = '/home/yujunzhe/nnsmith/outputs/2025-04-16'
    dirs = []
    
    for entry in os.listdir(base_dir):
        entry_path = os.path.join(base_dir, entry)
        if os.path.isdir(entry_path) and re.match(r'^\d{2}-\d{2}-\d{2}$', entry):
            try:
                h, m, s = map(int, entry.split('-'))
                if 0 <= h < 24 and 0 <= m < 60 and 0 <= s < 60:
                    dirs.append(entry)
            except ValueError:
                continue
    
    dirs_sorted = sorted(dirs, key=lambda x: tuple(map(int, x.split('-'))))
    selected_dirs = dirs_sorted[:591]
    
    total_gen = 0.0
    total_mat = 0.0
    
    for dir_name in selected_dirs:
        log_path = os.path.join(base_dir, dir_name, 'model_gen.log')
        try:
            with open(log_path, 'r') as f:
                lines = f.readlines()
                if not lines:
                    print(f"WARNING: Empty file {log_path}")
                    continue
                
                last_line = lines[-1].strip()
                gen_match = re.search(r'@Generation:\s*([\d.]+)s', last_line)
                mat_match = re.search(r'@Materialization:\s*([\d.]+)s', last_line)
                
                if gen_match and mat_match:
                    total_gen += float(gen_match.group(1))
                    total_mat += float(mat_match.group(1))
                else:
                    print(f"WARNING: Time data missing in {log_path}")
        except FileNotFoundError:
            print(f"ERROR: File not found {log_path}")
        except Exception as e:
            print(f"ERROR processing {log_path}: {str(e)}")
    
    print(f"Total Generation time: {total_gen:.2f} seconds")
    print(f"Total Materialization time: {total_mat:.2f} seconds")
    print(f"Total time: {total_gen + total_mat:.2f} seconds")

if __name__ == "__main__":
    main()