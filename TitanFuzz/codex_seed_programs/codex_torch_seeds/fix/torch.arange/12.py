'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.arange\ntorch.arange(start=0, end, step=1, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
import numpy as np
x = torch.arange(0, 10, 0.1)
print(x)
y = torch.arange(0, 10, 0.1, out=torch.FloatTensor())
print(y)
z = torch.arange(0, 10, 0.1, out=torch.cuda.FloatTensor())
print(z)
w = torch.arange(0, 10, 0.1, out=torch.cuda.FloatTensor())
print(w)
u = torch.arange(0, 10, 0.1, out=torch.cuda.FloatTensor())
print(u)