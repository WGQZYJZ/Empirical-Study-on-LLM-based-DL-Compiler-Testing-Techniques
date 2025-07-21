'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.digamma\ntorch.digamma(input, *, out=None)\n'
import torch
import numpy as np
input = torch.randn(3, 4)
print('Input data: \n', input)
output = torch.digamma(input)
print('Output data: \n', output)