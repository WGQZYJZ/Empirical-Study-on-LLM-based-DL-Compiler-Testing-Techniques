'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.i0\ntorch.special.i0(input, *, out=None)\n'
import torch
import numpy as np
input = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
print('Input: ', input)
output = torch.special.i0(input)
print('Output: ', output)