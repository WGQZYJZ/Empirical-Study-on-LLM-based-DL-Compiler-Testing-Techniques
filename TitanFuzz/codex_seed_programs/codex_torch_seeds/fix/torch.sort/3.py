'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sort\ntorch.sort(input, dim=-1, descending=False, stable=False, *, out=None)\n'
import torch
input = torch.randn(4, 5)
print('Input data:')
print(input)
print('\nOutput data:')
print(torch.sort(input, dim=(- 1), descending=False, stable=False))