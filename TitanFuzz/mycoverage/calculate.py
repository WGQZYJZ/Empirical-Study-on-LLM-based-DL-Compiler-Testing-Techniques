import re
import statistics

def extract_scores(content):
    pattern = r"Your code has been rated at (\d+\.\d+)/10"
    scores = re.findall(pattern, content)
    return [float(score) for score in scores]

def calculate_mean_and_variance(scores):
    if not scores:
        return 0.0, 0.0
    mean = statistics.mean(scores)
    variance = statistics.pvariance(scores)  
    return mean, variance

def main():
    with open("test_progarms_whitefox_1000/pylint.txt", "r", encoding="utf-8") as file:
        content = file.read()
    
    scores = extract_scores(content)
    print(f"Actually find {len(scores)} scores.")
    
    mean, variance = calculate_mean_and_variance(scores)
    print(f"average: {mean:.2f}")
    print(f"variance: {variance:.2f}")

if __name__ == "__main__":
    main()