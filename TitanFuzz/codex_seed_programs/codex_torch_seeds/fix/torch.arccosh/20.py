'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.arccosh\ntorch.arccosh(input, *, out=None)\n'
import torch
import numpy as np
a = torch.randn(1, 1)
print('The input data is:', a)
b = torch.arccosh(a)
print('The result of torch.arccosh is:', b)
c = np.arccosh(a.numpy())
print('The result of np.arccosh is:', c)