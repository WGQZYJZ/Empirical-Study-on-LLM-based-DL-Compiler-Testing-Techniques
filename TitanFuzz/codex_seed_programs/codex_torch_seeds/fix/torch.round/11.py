'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.round\ntorch.round(input, *, out=None)\n'
import torch
input = torch.rand(4, 4)
output = torch.round(input)
print('Input: \n', input)
print('Output: \n', output)