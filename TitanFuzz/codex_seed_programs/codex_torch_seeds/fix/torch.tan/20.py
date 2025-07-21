'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tan\ntorch.tan(input, *, out=None)\n'
import torch
import numpy as np
input = torch.randn(2, 3)
print('input = ', input)
output = torch.tan(input)
print('output = ', output)