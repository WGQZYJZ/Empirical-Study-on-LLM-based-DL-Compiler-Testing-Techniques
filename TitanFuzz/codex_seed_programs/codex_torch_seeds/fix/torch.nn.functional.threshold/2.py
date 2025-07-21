'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.threshold\ntorch.nn.functional.threshold(input, threshold, value, inplace=False)\n'
import torch
input = torch.randn(3, 3)
print('Input is:')
print(input)
output = torch.nn.functional.threshold(input, threshold=0.5, value=0.0)
print('Output is:')
print(output)