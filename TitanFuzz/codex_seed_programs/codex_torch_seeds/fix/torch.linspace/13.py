'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linspace\ntorch.linspace(start, end, steps, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
import torch
x = torch.linspace(start=0, end=10, steps=5)
print('x:', x)
x = torch.linspace(start=0, end=10, steps=5)
print('x:', x)
print('x.shape:', x.shape)
print('x.dtype:', x.dtype)
print('x.device:', x.device)
print('x.layout:', x.layout)
print('x.requires_grad:', x.requires_grad)