'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cumsum\ntorch.cumsum(input, dim, *, dtype=None, out=None)\n'
import torch
input = torch.randn(3, 4)
print('Input: ', input)
output = torch.cumsum(input, dim=1)
print('Output: ', output)