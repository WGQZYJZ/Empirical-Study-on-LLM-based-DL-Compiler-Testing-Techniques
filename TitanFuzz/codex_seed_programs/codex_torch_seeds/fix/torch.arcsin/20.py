'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.arcsin\ntorch.arcsin(input, *, out=None)\n'
import torch
import numpy as np
x = torch.randn(4, 4)
print(x)
torch.arcsin(x, out=None)
print(torch.arcsin(x, out=None))