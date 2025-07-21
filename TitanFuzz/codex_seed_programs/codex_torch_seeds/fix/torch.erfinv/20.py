'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.erfinv\ntorch.erfinv(input, *, out=None)\n'
import torch
input = torch.rand(4, 4)
print('Input:', input)
output = torch.erfinv(input)
print('Output:', output)