'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.deg2rad\ntorch.deg2rad(input, *, out=None)\n'
import torch
input = torch.randn(4, 4)
print('Input: ', input)
output = torch.deg2rad(input)
print('Output: ', output)