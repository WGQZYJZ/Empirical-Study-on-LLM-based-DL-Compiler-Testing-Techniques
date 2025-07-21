'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cos\ntorch.cos(input, *, out=None)\n'
import torch
input = torch.randn(4, 4)
print('Input: \n', input)
output = torch.cos(input)
print('Output: \n', output)