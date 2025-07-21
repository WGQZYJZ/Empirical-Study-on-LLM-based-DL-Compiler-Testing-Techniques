'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.count_nonzero\ntorch.count_nonzero(input, dim=None)\n'
import torch
input = torch.randn(4, 4)
print('Input: ', input)
print('Non-zero elements in input: ', torch.count_nonzero(input))