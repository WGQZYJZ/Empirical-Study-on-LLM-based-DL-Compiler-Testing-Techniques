'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cumprod\ntorch.cumprod(input, dim, *, dtype=None, out=None)\n'
import torch
input = torch.randn(4, 3)
print('Input: ', input)
output = torch.cumprod(input, dim=0)
print('Output: ', output)
output = torch.cumprod(input, dim=1)
print('Output: ', output)