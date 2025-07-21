'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.arange\ntorch.arange(start=0, end, step=1, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
x = torch.arange(0, 10, 0.5)
print(x)
y = torch.arange(0, 10, 0.5).reshape(4, 5)
print(y)
z = torch.arange(0, 10, 0.5).reshape(2, 2, 5)
print(z)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linspace\ntorch.linspace(start, end, steps=100, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
x = torch.linspace(0, 10, 5)
print(x)
y = torch.linspace(0, 10, 5).reshape(5, 1)
print(y)
z = torch.linspace(0, 10, 5).reshape(1, 5)
print(z)