'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.erfc\ntorch.special.erfc(input, *, out=None)\n'
import torch
import numpy as np
import torch
x = torch.randn(4, 4)
print('Input data: ', x)
y = torch.special.erfc(x)
print('Output data: ', y)