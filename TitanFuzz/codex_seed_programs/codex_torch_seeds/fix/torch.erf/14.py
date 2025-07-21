'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.erf\ntorch.erf(input, *, out=None)\n'
import torch
import numpy as np
x = torch.randn(4, 4)
print('Input: ', x)
y = torch.erf(x)
print('Output: ', y)