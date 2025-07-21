'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.floor\ntorch.floor(input, *, out=None)\n'
import torch
a = torch.randn(4)
print('Input:', a)
print('Output:', torch.floor(a))