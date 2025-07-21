'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.frac\ntorch.frac(input, *, out=None)\n'
import torch
x = torch.rand(4, 4)
print('Input:', x)
print('Output:', torch.frac(x))