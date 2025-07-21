'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.aminmax\ntorch.aminmax(input, *, dim=None, keepdim=False, out=None)\n'
import torch
import numpy as np
x = torch.randn(3, 4)
print('Input data: ', x)
print('torch.aminmax(x, dim=0, keepdim=False, out=None): ', torch.aminmax(x, dim=0, keepdim=False, out=None))
print('torch.aminmax(x, dim=0, keepdim=True, out=None): ', torch.aminmax(x, dim=0, keepdim=True, out=None))
print('torch.aminmax(x, dim=1, keepdim=False, out=None): ', torch.aminmax(x, dim=1, keepdim=False, out=None))