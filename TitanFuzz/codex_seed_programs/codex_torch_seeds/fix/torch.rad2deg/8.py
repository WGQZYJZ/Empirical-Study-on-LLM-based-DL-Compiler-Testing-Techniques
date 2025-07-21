'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.rad2deg\ntorch.rad2deg(input, *, out=None)\n'
import torch
input = torch.rand(4)
print('input: ', input)
output = torch.rad2deg(input)
print('output: ', output)