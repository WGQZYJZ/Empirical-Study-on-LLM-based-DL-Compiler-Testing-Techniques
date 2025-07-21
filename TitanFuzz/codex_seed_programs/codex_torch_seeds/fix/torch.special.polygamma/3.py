'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.polygamma\ntorch.special.polygamma(n, input, *, out=None)\n'
import torch
input = torch.randn(3, 3)
print('Input:', input)
output = torch.special.polygamma(1, input)
print('Output:', output)