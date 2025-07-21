'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.le\ntorch.le(input, other, *, out=None)\n'
import torch
input = torch.randn(3, requires_grad=True)
other = torch.tensor([1.0, 2.0, 3.0])
output = torch.le(input, other)
print('input:', input)
print('other:', other)
print('output:', output)