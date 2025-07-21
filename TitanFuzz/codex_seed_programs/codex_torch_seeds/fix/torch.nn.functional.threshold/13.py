'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.threshold\ntorch.nn.functional.threshold(input, threshold, value, inplace=False)\n'
import torch
input = torch.randn(2, 3)
print(input)
output = torch.nn.functional.threshold(input, 0.5, 0)
print(output)