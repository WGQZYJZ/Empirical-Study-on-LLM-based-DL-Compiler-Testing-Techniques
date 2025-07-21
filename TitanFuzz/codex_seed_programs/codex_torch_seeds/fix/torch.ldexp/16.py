'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.ldexp\ntorch.ldexp(input, other, *, out=None)\n'
import torch
input = torch.rand(4, 4)
other = torch.randint(low=1, high=10, size=(4, 4))
output = torch.ldexp(input, other)
print('input:', input)
print('other:', other)
print('output:', output)