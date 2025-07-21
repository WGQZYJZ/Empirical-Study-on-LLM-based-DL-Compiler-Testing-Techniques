'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.arcsinh\ntorch.arcsinh(input, *, out=None)\n'
import torch
import numpy as np
a = torch.randn(4, 4)
print('a = ', a)
print('arcsinh(a) = ', torch.arcsinh(a))