'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.ldexp\ntorch.ldexp(input, other, *, out=None)\n'
import torch
input = torch.randn(4)
other = torch.tensor([1, 2, 3, 4], dtype=torch.float)
print(input)
print(other)
print(torch.ldexp(input, other))
print(torch.ldexp_(input, other))
print(input)