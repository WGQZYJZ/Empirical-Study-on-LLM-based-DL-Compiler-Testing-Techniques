'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.polygamma\ntorch.polygamma(n, input, *, out=None)\n'
import torch
input = torch.rand(2, 3)
print('Input:', input)
output = torch.polygamma(1, input)
print('Output:', output)