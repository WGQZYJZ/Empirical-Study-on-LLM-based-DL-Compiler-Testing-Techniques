'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.rsqrt\ntorch.rsqrt(input, *, out=None)\n'
import torch
input = torch.randn(1, 3, requires_grad=True)
print('input = ', input)
output = torch.rsqrt(input)
print('output = ', output)