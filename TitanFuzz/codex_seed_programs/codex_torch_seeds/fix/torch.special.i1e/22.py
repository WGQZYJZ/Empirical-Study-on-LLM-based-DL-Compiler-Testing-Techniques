'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.i1e\ntorch.special.i1e(input, *, out=None)\n'
import torch
input = torch.rand(1, 3)
print(input)
print('\nOutput: ')
print(torch.special.i1e(input))