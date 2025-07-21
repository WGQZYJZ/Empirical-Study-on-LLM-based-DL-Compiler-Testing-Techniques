'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fmax\ntorch.fmax(input, other, *, out=None)\n'
import torch
import numpy as np
input = torch.randn(2, 3)
other = torch.randn(2, 3)
print(torch.fmax(input, other))
input = torch.randn(2, 3)
other = torch.randn(2, 3)
print(torch.fmin(input, other))
input = torch.randn(2, 3)
other = torch.randn(2, 3)
print(torch.fmod(input, other))
input = torch.randn(2, 3)
other = torch.randn(2, 3)
print(torch.fmod(input, other))
input = torch.randn(2, 3)