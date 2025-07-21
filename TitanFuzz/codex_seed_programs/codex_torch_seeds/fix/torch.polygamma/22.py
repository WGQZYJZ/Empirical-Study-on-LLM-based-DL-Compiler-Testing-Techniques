'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.polygamma\ntorch.polygamma(n, input, *, out=None)\n'
import torch
import numpy as np
input = torch.randn(4, 4)
print('Input: ', input)
output = torch.polygamma(5, input)
print('Output: ', output)