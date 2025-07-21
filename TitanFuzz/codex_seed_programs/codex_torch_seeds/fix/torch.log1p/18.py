'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.log1p\ntorch.log1p(input, *, out=None)\n'
import torch
input = torch.randn(1, 2, 3)
result = torch.log1p(input)
print('Input: {}'.format(input))
print('Result: {}'.format(result))