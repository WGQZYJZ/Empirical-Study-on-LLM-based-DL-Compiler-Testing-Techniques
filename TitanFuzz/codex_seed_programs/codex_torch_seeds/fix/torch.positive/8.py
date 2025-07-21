'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.positive\ntorch.positive(input)\n'
import torch
input = torch.randn(2, 3)
print('Input: \n', input)
output = torch.positive(input)
print('Output: \n', output)