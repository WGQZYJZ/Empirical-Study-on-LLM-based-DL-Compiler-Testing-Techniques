'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cumprod\ntorch.cumprod(input, dim, *, dtype=None, out=None)\n'
import torch
input = torch.randn(5, 2, 3)
print('input: ', input)
output = torch.cumprod(input, dim=1)
print('output: ', output)