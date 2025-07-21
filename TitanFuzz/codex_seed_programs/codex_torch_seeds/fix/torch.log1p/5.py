'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.log1p\ntorch.log1p(input, *, out=None)\n'
import torch
input = torch.randn(4, 4)
print('Input data: ', input)
out = torch.log1p(input)
print('Output: ', out)