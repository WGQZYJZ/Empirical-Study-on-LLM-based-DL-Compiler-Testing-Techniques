import re

def count_ratings(file_path):
    pattern = re.compile(r"Your code has been rated at \d+\.\d+/10")
    count = 0
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                if pattern.search(line.strip()):
                    count += 1
        return count
    except FileNotFoundError:
        return -1 

if __name__ == "__main__":
    file_path = "test_progarms_whitefox_all/pylint.txt"  
    result = count_ratings(file_path)
    
    if result >= 0:
        print(f"Find numbers: {result}")
    else:
        print("Error.")