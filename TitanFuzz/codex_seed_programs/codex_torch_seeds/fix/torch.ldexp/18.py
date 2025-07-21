'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.ldexp\ntorch.ldexp(input, other, *, out=None)\n'
import torch
import torch
input = torch.randn(2, 3)
other = torch.randn(2, 3)
torch.ldexp(input, other)