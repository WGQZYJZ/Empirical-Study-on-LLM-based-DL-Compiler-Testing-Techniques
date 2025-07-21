'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cumprod\ntorch.cumprod(input, dim, *, dtype=None, out=None)\n'
import torch
input = torch.randn(2, 3, 4)
print('Input tensor: ', input)
print('Cumulative product of the input tensor: ', torch.cumprod(input, dim=1))