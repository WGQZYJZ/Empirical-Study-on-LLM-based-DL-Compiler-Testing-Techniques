'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.minimum\ntorch.minimum(input, other, *, out=None)\n'
import torch
input = torch.randn(3, 1)
other = torch.randn(3, 1)
print('input:', input)
print('other:', other)
minimum = torch.minimum(input, other)
print('minimum:', minimum)