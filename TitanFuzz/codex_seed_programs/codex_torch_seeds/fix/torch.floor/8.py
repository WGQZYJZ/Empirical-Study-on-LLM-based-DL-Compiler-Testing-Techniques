'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.floor\ntorch.floor(input, *, out=None)\n'
import torch
input = torch.randn(1, 1)
print('Input data: ', input)
output = torch.floor(input)
print('Output: ', output)