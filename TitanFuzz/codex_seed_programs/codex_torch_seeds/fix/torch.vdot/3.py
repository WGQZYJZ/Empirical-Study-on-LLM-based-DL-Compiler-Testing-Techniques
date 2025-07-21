'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.vdot\ntorch.vdot(input, other, *, out=None)\n'
import torch
input = torch.randn(10, requires_grad=True)
other = torch.randn(10)
print('input: ', input)
print('other: ', other)
print('torch.vdot(input, other): ', torch.vdot(input, other))