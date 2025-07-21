'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.igamma\ntorch.igamma(input, other, *, out=None)\n'
import torch
import numpy as np
import torch
input = torch.randn(1, 3)
other = torch.randn(1, 3)
output = torch.igamma(input, other)
print(output)