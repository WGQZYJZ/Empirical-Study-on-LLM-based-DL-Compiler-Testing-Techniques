'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.logspace\ntorch.logspace(start, end, steps, base=10.0, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
x = torch.arange(1, 10, dtype=torch.float)
print('Input: ', x)
y = torch.logspace(start=0, end=2, steps=5)
print('Output: ', y)