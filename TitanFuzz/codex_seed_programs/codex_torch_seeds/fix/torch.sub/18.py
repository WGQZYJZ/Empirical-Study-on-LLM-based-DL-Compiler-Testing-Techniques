'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sub\ntorch.sub(input, other, *, alpha=1, out=None)\n'
import torch
import numpy as np
input = torch.randn(2, 3)
other = torch.randn(2, 3)
output = torch.sub(input, other)
print('input:', input)
print('other:', other)
print('output:', output)