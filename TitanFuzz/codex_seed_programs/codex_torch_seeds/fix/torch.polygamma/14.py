'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.polygamma\ntorch.polygamma(n, input, *, out=None)\n'
import torch
import numpy as np
input = torch.tensor([[1, 2, 3], [4, 5, 6]])
print('Input: ', input)
output = torch.polygamma(5, input)
print('Output: ', output)