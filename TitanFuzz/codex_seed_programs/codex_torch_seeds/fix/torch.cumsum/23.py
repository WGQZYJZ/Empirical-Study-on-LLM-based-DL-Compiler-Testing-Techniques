'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cumsum\ntorch.cumsum(input, dim, *, dtype=None, out=None)\n'
import torch
input = torch.randn(2, 3)
print('Input:', input)
print('Output:', torch.cumsum(input, dim=0))
print('Output:', torch.cumsum(input, dim=1))
print('Output:', torch.cumsum(input, dim=1, dtype=torch.float))
print('Output:', torch.cumsum(input, dim=0, out=torch.zeros_like(input)))