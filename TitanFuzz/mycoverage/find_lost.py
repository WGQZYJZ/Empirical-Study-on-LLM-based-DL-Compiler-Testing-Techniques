import re

def find_missing_ratings_corrected(file_path):
    analysis_pattern = re.compile(r'# Analysis for: (.+?\.py)')
    rating_pattern = re.compile(r'Your code has been rated at \d+\.\d+/10')
    
    missing_entries = []    
    current_entry = []       
    current_file = None      
    has_rating = False       
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:

                analysis_match = analysis_pattern.search(line)
                if analysis_match:

                    if current_file is not None:
                        if not has_rating:
                            missing_entries.append((''.join(current_entry), current_file))

                        current_entry = []
                        has_rating = False
                    

                    current_file = analysis_match.group(1)
                    current_entry.append(line)
                    continue
                

                if current_file is not None:
                    current_entry.append(line)

                    if rating_pattern.search(line):
                        has_rating = True
            
            if current_file is not None and not has_rating:
                missing_entries.append((''.join(current_entry), current_file))
                
    except FileNotFoundError:
        print(f"Error: File {file_path} does not exist")
        return []
    
    return missing_entries

if __name__ == "__main__":
    target_file = "test_progarms_whitefox_all/pylint.txt"  
    results = find_missing_ratings_corrected(target_file)
    
    if results:
        print(f"Find {len(results)} missing folder")
        for idx, (content, filename) in enumerate(results, 1):
            print(f"\n{idx}. missing file: {filename}")
            print("content:")
            summary = '\n'.join(content.split('\n')[:5]) 
            print(summary)
            print("-" * 60)
        with open("accurate_missing.log", "w", encoding='utf-8') as f:
            for content, filename in results:
                f.write(f"[Missing file]{filename}\n")
                f.write(f"[Complete content]\n{content}\n\n")
        print("\nThe full results have been saved to accurate_missing.log") 
    else:
        print("All analysis entries include rating information")