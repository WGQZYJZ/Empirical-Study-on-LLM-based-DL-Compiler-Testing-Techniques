'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.threshold\ntorch.nn.functional.threshold(input, threshold, value, inplace=False)\n'
import torch
input = torch.randn(5, 5)
print(input)
threshold = 0
value = 0
output = torch.nn.functional.threshold(input, threshold, value)
print(output)