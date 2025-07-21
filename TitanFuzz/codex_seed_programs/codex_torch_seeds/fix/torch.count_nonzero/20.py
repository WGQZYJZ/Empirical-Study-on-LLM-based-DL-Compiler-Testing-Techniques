'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.count_nonzero\ntorch.count_nonzero(input, dim=None)\n'
import torch
input = torch.randn((3, 3))
print('Input: ', input)
print('Count nonzero elements: ', torch.count_nonzero(input))
print('Count nonzero elements in dim 0: ', torch.count_nonzero(input, dim=0))
print('Count nonzero elements in dim 1: ', torch.count_nonzero(input, dim=1))