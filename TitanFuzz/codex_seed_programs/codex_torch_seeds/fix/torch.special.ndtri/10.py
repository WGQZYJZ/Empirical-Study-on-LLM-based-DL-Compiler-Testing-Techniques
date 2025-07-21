'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.ndtri\ntorch.special.ndtri(input, *, out=None)\n'
import torch
input = torch.randn(1, 5)
output = torch.special.ndtri(input)
print('input = \n', input)
print('output = \n', output)